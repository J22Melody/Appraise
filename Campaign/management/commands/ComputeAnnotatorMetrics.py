from collections import OrderedDict, defaultdict
from json import loads

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from Campaign.models import Campaign
from EvalData.models import DirectAssessmentResult, DirectAssessmentTask


# pylint: disable=C0111,C0330,E1101
class Command(BaseCommand):
    help = 'Computes annotator reliability metrics'

    def add_arguments(self, parser):
        parser.add_argument(
          'campaign_name', type=str,
          help='Name of the campaign you want to process data for'
        )
        parser.add_argument(
          '--csv-file', type=str,
          help='CSV file containing annotation data'
        )
        parser.add_argument(
          '--exclude-ids', type=str,
          help='User IDs which should be ignored'
        )
        parser.add_argument(
          '--export-csv', action='store_true',
          help='Exports CSV data in machine readable format'
        )
        parser.add_argument(
          '--chk-threshold', type=float, default=0.5,
          help='Absolute z threshold below which CHK items are equal'
        )
        # TODO: add argument to specify batch user

    def handle(self, *args, **options):
        campaign_name = options['campaign_name']
        csv_file = options['csv_file']
        exclude_ids = [x.lower() for x in options['exclude_ids'].split(',')] \
          if options['exclude_ids'] else []
        export_csv = options['export_csv']
        chk_threshold = options['chk_threshold']

        user_scores = defaultdict(list)
        if csv_file:
            if not export_csv:
                _msg = 'Processing annotations in file {0}\n\n'.format(csv_file)
                self.stdout.write(_msg)

            # Need to load data from CSV file and bring into same
            # format as would have been produced by the call to
            # get_system_scores().
            #
            # CSV has this format
            # zhoeng0802,GOOG_WMT2009_Test.chs-enu.txt,678,CHK,zho,eng,76,1511470503.271,1511470509.224

            import csv
            with open(csv_file) as input_file:
                csv_reader = csv.reader(input_file)
                for csv_line in csv_reader:
                    _user_id = csv_line[0]
                    if _user_id.lower() in exclude_ids:
                        continue

                    _system_id = csv_line[1]
                    _segment_id = csv_line[2]
                    _type = csv_line[3]
                    _src = csv_line[4]
                    _tgt = csv_line[5]
                    _score = int(csv_line[6])
                    _key = '{0}-{1}-{2}'.format(
                      _src, _tgt, _user_id
                    )

                    user_scores[_key].append((_segment_id, _system_id, _type,  _score))

        else:
            # Identify Campaign instance for given name
            campaign = Campaign.objects.filter(campaignName=campaign_name).first()
            if not campaign:
                if not export_csv:
                    _msg = 'Failure to identify campaign {0}'.format(campaign_name)
                    self.stdout.write(_msg)
                return

            csv_data = DirectAssessmentResult.get_system_data(campaign.id, extended_csv=True)

            for csv_line in csv_data:
                _user_id = csv_line[0]
                if _user_id.lower() in exclude_ids:
                    continue

                _system_id = csv_line[1]
                _segment_id = csv_line[2]
                _type = csv_line[3]
                _src = csv_line[4]
                _tgt = csv_line[5]
                _score = int(csv_line[6])
                _key = '{0}-{1}-{2}'.format(
                  _src, _tgt, _user_id
                )

                user_scores[_key].append((_segment_id, _system_id, _type,  _score))

        segments_by_user = defaultdict(list)
        for key, values in user_scores.items():
            for value in values:
                if not value[0] in segments_by_user[key]:
                    segments_by_user[key].append(value[0])

        user_means = defaultdict(float)
        user_stdev = defaultdict(float)

        from math import sqrt
        for key, values in user_scores.items():
            _scores = [x[3] for x in values]
            user_means[key] = sum(_scores) / len(_scores) if len(_scores) else 0
            user_stdev[key] = sqrt( sum( ( (x - user_means[key]) ** 2 / (len(_scores) - 1) ) for x in _scores ) )

        user_z_scores = defaultdict(list)
        for key, values in user_scores.items():
            for value in values:
                z_score = (value[3] - user_means[key]) / user_stdev[key]
                user_z_scores[key].append((value[0], value[1], value[2], z_score))

        user_scores = user_z_scores

        metrics = defaultdict(list)
        for key, values in user_scores.items():
            _sorted = [(x[3], x[2]) for x in values]
            _sorted.sort()

            _median = list(sorted(set([x[0] for x in _sorted])))
            _median_score = _median[len(_median) // 2]

            _lower_refs = 0
            _upper_refs = 0
            for item in _sorted:
                if item[1] != 'REF':
                    continue

                if item[0] > _median_score:
                    _upper_refs += 1
                else:
                    _lower_refs += 1

            metrics[key].append((_lower_refs, _upper_refs))

            _scores = defaultdict(list)
            for x in values:
                if x[2] not in ('TGT', 'CHK'):
                    continue

                _key = '{0}-{1}'.format(x[0], x[1])
                _fourScore = x[3] # min(int(x[3]/25.) + 1, 4)
                _scores[_key].append((_fourScore, x[2]))

            _potential = 0
            _matches = 0
            for item in _scores.items():
                if len(item[1]) == 2:
                    _potential += 1
                    _data = item[1]
                    _data.sort(key=lambda x: x[1])
                    # if _data[0][0] == _data[1][0]:
                    if abs(_data[0][0] - _data[1][0]) < chk_threshold:
                        _matches += 1

            metrics[key].append((_matches, _potential))

            _scores = defaultdict(list)
            for x in values:
                if x[2] not in ('TGT', 'BAD'):
                    continue

                _key = '{0}-{1}'.format(x[0], x[1])
                _scores[_key].append((x[3], x[2]))

            deltas = []
            for item in _scores.items():
                if len(item[1]) == 2:
                    _data = item[1]
                    _data.sort(key=lambda x: x[1])

                    deltas.append(_data[0][0] - _data[1][0])

            metrics[key].append(deltas)
            metrics[key].append(len(value))

        if export_csv:
            _fields = (
              'UserID', 'Ref', 'Chk', 'Bad', 'Count'
            )
            _header = ','.join(_fields)
            print(_header)

        for key in sorted(metrics.keys()):
            value = metrics[key]
            metric1 = value[0][1] - value[0][0]
            metric2 = value[1][0] / value[1][1] if value[1][1] else 0
            metric3 = 0
            metric4 = len(segments_by_user[key])

            try:
                from scipy import stats
                t, pvalue = stats.wilcoxon(value[2], correction=True)
                metric3 = pvalue

            except ImportError:
                pass

            if not export_csv:
                print("{0}\t{1:2d}\t{2:.2f}\t{3:f}\t{4:3d}".format(
                  key, metric1, metric2, metric3, metric4)
                )

            else:
                _data = (key, str(metric1), str(metric2), str(metric3), str(metric4))
                _line = ','.join(_data)
                _line = _line.replace('nan', '0.000000')

        if not export_csv:
            print('\nExcluded IDs: {0}\n'.format(', '.join(exclude_ids)))
