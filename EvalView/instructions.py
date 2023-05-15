#! /bin/python


SL_VIDEO_INSTRUCTIONS_TEMPLATE_SEGMENT = """<center>
    <button onclick="show_video_instructions_segment()" class="btn btn-default button-margin" id="btn-show-video-instructions-segment" texthide="{text_hide}" textshow="{text_show}">{text_show}</button>

    <iframe width="560" id="iframe-video-instructions-segment" height="315" src="{url}"
        title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; 
        gyroscope; picture-in-picture; web-share" allowfullscreen style="display:none"></iframe>
</center>
"""


SL_VIDEO_INSTRUCTIONS_TEMPLATE_DOCUMENT = """<center>
    <button type="button" onclick="show_video_instructions_document()" class="btn btn-default button-margin" id="btn-show-video-instructions-document" texthide="{text_hide}" textshow="{text_show}">{text_show}</button>

    <iframe width="560" id="iframe-video-instructions-document" height="315" src="{url}"
        title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; 
        gyroscope; picture-in-picture; web-share" allowfullscreen style="display:none"></iframe>
</center>
"""


sl_video_instructions_urls = {
    "text_to_sign": {
        "segment": {
            "sgg": "https://www.youtube.com/embed/lQaQmAo8RrA",
            "ise": "https://www.youtube.com/embed/ZTGDPyc-yr0",
            "fsl": "https://www.youtube.com/embed/2a3XvKwQaJI"
        },
        "document": {
            "sgg": "https://www.youtube.com/embed/opsbXBLvv7I",
            "ise": "https://www.youtube.com/embed/uxRzGovPZsM",
            "fsl": "https://www.youtube.com/embed/4vcnpxBFYa4"
        }
    },
    "sign_to_text": {
        "segment": {
            "sgg": "https://www.youtube.com/embed/zWQ5eyu7Z4o",
            "ise": "https://www.youtube.com/embed/ZlcecwjewIs",
            "fsl": "https://www.youtube.com/embed/C2q12OfKPX0"
        },
        "document": {
            "sgg": "https://www.youtube.com/embed/o4tVcE929mk",
            "ise": "https://www.youtube.com/embed/M-iJSpjtPuY",
            "fsl": "https://www.youtube.com/embed/sWyPg9lxrdQ"
        }
    }
}

button_texts = {
    "eng": {
        "hide": "Hide sign language instructions",
        "show": "Show sign language instructions"
    },
    "deu": {
        "hide": "Anleitung in Gebärdensprache ausblenden",
        "show": "Anleitung in Gebärdensprache anzeigen"
    },
    "fra": {
        "hide": "Masquer les instructions en langue des signes",
        "show": "Afficher les instructions en langue des signes"
    },
    "ita": {
        "hide": "Nnascondere le istruzioni in lingua dei segni ",
        "show": "Mostrare le istruzioni in lingua dei segni "
    },
}


def get_video_instructions(direction: str, level: str, sign_language: str, ui_language: str) -> str:

    url = sl_video_instructions_urls[direction][level][sign_language]

    text_hide = button_texts[ui_language]["hide"]
    text_show = button_texts[ui_language]["show"]

    if level == "segment":
        template = SL_VIDEO_INSTRUCTIONS_TEMPLATE_SEGMENT
    else:
        template = SL_VIDEO_INSTRUCTIONS_TEMPLATE_DOCUMENT

    return template.format(url=url, text_hide=text_hide, text_show=text_show)


def get_sign_language_instructions(ui_language, text_to_sign, block_items, source_language, target_language,
                                   source_language_code, target_language_code, add_video_instructions: bool):

    if ui_language == "deu":
        if text_to_sign:
            priming_question_texts = [
                'Unten sehen Sie ein Dokument mit {0} Sätzen auf Deutsch (linke Spalten) '
                'und die entsprechenden möglichen Übersetzungen in Deutschschweizer '
                'Gebärdensprache (DSGS) (rechte Spalten). Bewerten Sie jede mögliche '
                'Übersetzung des Satzes im Kontext des Dokuments. '
                'Sie können bereits bewertete Sätze jederzeit durch Anklicken eines '
                'Quelltextes erneut aufrufen und die Bewertung aktualisieren.'.format(
                    len(block_items) - 1,
                ),
            ]

        else:
            priming_question_texts = [
                'Unten sehen Sie ein Dokument mit {0} Sätzen in Deutschschweizer '
                'Gebärdensprache (DSGS) (linke Spalten) und die entsprechenden möglichen '
                'Übersetzungen auf Deutsch (rechte Spalten). Bewerten Sie jede mögliche '
                'Übersetzung des Satzes im Kontext des Dokuments. '
                'Sie können bereits bewertete Sätze jederzeit durch Anklicken eines '
                'Eingabevideos erneut aufrufen und die Bewertung aktualisieren.'.format(
                    len(block_items) - 1,
                ),
            ]

        document_question_texts = [
            'Bitte bewerten Sie die Übersetzungsqualität des gesamten Dokuments. '
            '(Sie können das Dokument erst bewerten, nachdem Sie zuvor alle Sätze '
            'einzeln bewertet haben.)',
        ]

    elif ui_language == "fra":
        if text_to_sign:
            priming_question_texts = [
                'Vous voyez ci-dessous un document avec {0} phrases en français (colonnes '
                'de gauche) et leurs traductions candidates correspondantes en langue des '
                'signes française (LSF) (colonnes de droite). Veuillez attribuer un score '
                'à chaque traduction possible de la phrase dans le contexte du document. '
                'Vous pouvez revisiter les phrases déjà évaluées et mettre à jour leurs '
                'scores à tout moment en cliquant sur un texte source.'.format(
                    len(block_items) - 1,
                ),
            ]
        else:
            priming_question_texts = [
                'Vous voyez ci-dessous un document avec {0} phrases en langue des signes '
                'française (LSF) (colonnes de gauche) et leurs traductions candidates '
                'correspondantes en français (colonnes de droite). Veuillez attribuer un '
                'score à chaque traduction possible de la phrase dans le contexte du document. '
                'Vous pouvez revisiter les phrases déjà évaluées et mettre à jour leurs '
                'scores à tout moment en cliquant sur une vidéo source.'.format(
                    len(block_items) - 1,
                ),
            ]

        document_question_texts = [
            "Veuillez noter la qualité globale de la traduction du document (vous ne pouvez noter "
            "l'ensemble du document qu'après avoir noté toutes les phrases individuelles).",
        ]

    elif ui_language == "ita":
        if text_to_sign:
            priming_question_texts = [
                'Qui sotto trovate un documento con {0} frasi in italiano (colonne di sinistra) e le'
                'corrispondenti possibili traduzioni nella lingua dei segni italiana '
                '(LIS) (colonne di destra). Valutate '
                'ogni possibile traduzione della frase nel contesto del documento. Potete rivedere '
                'le frasi valutate in precedenza e aggiornarne le valutazioni in qualsiasi momento '
                'cliccando sul testo sorgente.'.format(
                    len(block_items) - 1,
                ),
            ]
        else:
            priming_question_texts = [
                'Qui sotto trovate un documento con {0} frasi nella lingua dei segni italiana '
                '(LIS) (colonne di sinistra) e le corrispondenti possibili traduzioni in '
                'italiano (colonne di destra). Valutate ogni possibile traduzione della '
                'frase nel contesto del documento. Potete rivedere le frasi valutate in '
                'precedenza e aggiornarne le valutazioni in qualsiasi momento cliccando '
                'su un video sorgente.'.format(
                    len(block_items) - 1,
                ),
            ]

        document_question_texts = [
            "Si prega di valutare la qualità della traduzione dell'intero documento. "
            "Non è possibile valutare il documento finché non si è valutato ogni frase singolarmente.",
        ]

    else:
        assert ui_language == "eng"

        if text_to_sign:
            priming_question_texts = [
                'Below you see a document with {0} sentences in {1} (left columns) and '
                'their corresponding candidate translations in '
                '{2} (right columns). Score each candidate '
                'sentence translation in the document context. You may revisit already scored '
                'sentences and update their scores at any time by clicking on a source text.'.format(
                    len(block_items) - 1,
                    source_language,
                    target_language,
                ),
            ]
        else:
            priming_question_texts = [
                'Below you see a document with {0} sentences in '
                '{1} (left columns) '
                'and their corresponding candidate translations in {2} (right columns). '
                'Score each candidate sentence translation in the document context. You may revisit '
                'already scored sentences and update their scores at any time by clicking on a source video.'.format(
                    len(block_items) - 1,
                    source_language,
                    target_language,
                ),
            ]

        document_question_texts = [
            'Please score the overall document translation quality (you can score the whole document only '
            'after scoring all individual sentences first).',
        ]

    if add_video_instructions:

        if text_to_sign:
            direction = "text_to_sign"
            sign_language = target_language_code
        else:
            direction = "sign_to_text"
            sign_language = source_language_code

        # on segment level

        video_string_segment = get_video_instructions(direction=direction,
                                                      level="segment",
                                                      sign_language=sign_language,
                                                      ui_language=ui_language)

        priming_question_texts = [video_string_segment] + priming_question_texts

        # on document level

        video_string_document = get_video_instructions(direction=direction,
                                                       level="document",
                                                       sign_language=sign_language,
                                                       ui_language=ui_language)

        document_question_texts = [video_string_document] + document_question_texts

    return priming_question_texts, document_question_texts
