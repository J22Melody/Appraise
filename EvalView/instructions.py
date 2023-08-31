#! /bin/python


SL_VIDEO_INSTRUCTIONS_TEMPLATE_SEGMENT_YOUTUBE = """<center>
    <button onclick="show_video_instructions_segment()" class="btn btn-default button-margin" id="btn-show-video-instructions-segment" texthide="{text_hide}" textshow="{text_show}">{text_show}</button>

    <iframe width="560" id="iframe-video-instructions-segment" height="315" src="{url}"
        title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; 
        gyroscope; picture-in-picture; web-share" allowfullscreen style="display:none"></iframe>
</center>
"""


SL_VIDEO_INSTRUCTIONS_TEMPLATE_DOCUMENT_YOUTUBE = """<center>
    <button type="button" onclick="show_video_instructions_document()" class="btn btn-default button-margin" id="btn-show-video-instructions-document" texthide="{text_hide}" textshow="{text_show}">{text_show}</button>

    <iframe width="560" id="iframe-video-instructions-document" height="315" src="{url}"
        title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; 
        gyroscope; picture-in-picture; web-share" allowfullscreen style="display:none"></iframe>
</center>
"""


SL_VIDEO_INSTRUCTIONS_TEMPLATE_SEGMENT_KALTURA = """<center>
    <button onclick="show_video_instructions_segment()" class="btn btn-default button-margin" id="btn-show-video-instructions-segment" texthide="{text_hide}" textshow="{text_show}">{text_show}</button>

    <iframe width="608" height="402" id="iframe-video-instructions-segment" src="{url}"
        class="kmsembed" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" referrerPolicy="no-referrer-when-downgrade"
        sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" style="display:none" title="Kaltura player"></iframe>
</center>
"""


SL_VIDEO_INSTRUCTIONS_TEMPLATE_DOCUMENT_KALTURA = """<center>
    <button type="button" onclick="show_video_instructions_document()" class="btn btn-default button-margin" id="btn-show-video-instructions-document" texthide="{text_hide}" textshow="{text_show}">{text_show}</button>

    <iframe width="608" height="402" id="iframe-video-instructions-document" src="{url}"
        class="kmsembed" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" referrerPolicy="no-referrer-when-downgrade"
        sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" style="display:none" title="Kaltura player"></iframe>
</center>
"""


sl_video_instructions_urls_youtube = {
    "text_to_sign": {
        "segment": {
            "sgg": "https://www.youtube.com/embed/b1-N6op9Ozk",
            "ise": "https://www.youtube.com/embed/9ujx9aUNMeM",
            "fsl": "https://www.youtube.com/embed/koSiyyXn2Qs"
        },
        "document": {
            "sgg": "https://www.youtube.com/embed/rWfITo0TuOE",
            "ise": "https://www.youtube.com/embed/ULwsjzEUUVI",
            "fsl": "https://www.youtube.com/embed/03bW-qQqcNg"
        }
    },
    "sign_to_text": {
        "segment": {
            "sgg": "https://www.youtube.com/embed/_kPvKZKZDPw",
            "ise": "https://www.youtube.com/embed/w9YdbhzH10c",
            "fsl": "https://www.youtube.com/embed/Yl9i2KGUtvI"
        },
        "document": {
            "sgg": "https://www.youtube.com/embed/x2FEUfg-h6U",
            "ise": "https://www.youtube.com/embed/F8GpkALmu4Q",
            "fsl": "https://www.youtube.com/embed/WNcdMahoyeo"
        }
    }
}


sl_video_instructions_urls_kaltura = {
    "text_to_sign": {
        "segment": {
            "sgg": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_ginojjwt/uiConfId/23448425/st/0",
            "ise": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_m8sapvzb/uiConfId/23448425/st/0",
            "fsl": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_q1uhudq3/uiConfId/23448425/st/0",
            "bfi": "",
            "gsg": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_hjtvkp1i/uiConfId/23448425/st/0",
        },
        "document": {
            "sgg": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_dea3l9cz/uiConfId/23448425/st/0",
            "ise": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_tzfugwt8/uiConfId/23448425/st/0",
            "fsl": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_ns4vzs3q/uiConfId/23448425/st/0",
            "bfi": "",
            "gsg": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_l6md75up/uiConfId/23448425/st/0",
        }
    },
    "sign_to_text": {
        "segment": {
            "sgg": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_1ccvo9ou/uiConfId/23448425/st/0",
            "ise": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_7h5su6he/uiConfId/23448425/st/0",
            "fsl": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_rc33fcid/uiConfId/23448425/st/0",
            "bfi": "",
            "gsg": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_95mb8yq6/uiConfId/23448425/st/0",
        },
        "document": {
            "sgg": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_zao6hxoe/uiConfId/23448425/st/0",
            "ise": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_r1j19lk5/uiConfId/23448425/st/0",
            "fsl": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_akamang4/uiConfId/23448425/st/0",
            "bfi": "",
            "gsg": "https://uzh.mediaspace.cast.switch.ch/embed/secure/iframe/entryId/0_gmvd2djb/uiConfId/23448425/st/0",
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
        "hide": "Nascondi le istruzioni in lingua dei segni",
        "show": "Mostra le istruzioni in lingua dei segni"
    },
}


language_names_per_ui_language = {
    "eng": {
        "deu": "German",
        "eng": "English",
        "fra": "French",
        "ita": "Italian",
        "sgg": "Swiss German Sign Language (DSGS)",
        "ise": "Italian Sign Language (LIS)",
        "fsl": "French Sign Language (LSF)",
        "bfi": "British Sign Language (BSL)",
        "gsg": "German Sign Language (DGS)",
    },
    "deu": {
        # modified for correct German case
        "deu": "Deutsch",
        "eng": "Englisch",
        "fra": "Französisch",
        "ita": "Italienisch",
        "sgg": "Schweizerdeutscher Gebärdensprache (DSGS)",
        "ise": "Italienischer Gebärdensprache (LIS)",
        "fsl": "Französischer Gebärdensprache (LSF)",
        "bfi": "Britischer Gebärdensprache (BSL)",
        "gsg": "Deutscher Gebärdensprache (DGS)",
    },
    "fra": {
        "deu": "allemand",
        "eng": "anglais",
        "fra": "français",
        "ita": "italien",
        "sgg": "",
        "ise": "",
        "fsl": "langue des signes française (LSF)",
        "bfi": "",
        "gsg": "",
    },
    "ita": {
        "deu": "tedesco",
        "eng": "inglese",
        "fra": "francese",
        "ita": "italiano",
        "sgg": "",
        "ise": "lingua dei segni italiana (LIS)",
        "fsl": "",
        "bfi": "",
        "gsg": "",
    },
}


def get_video_instructions(direction: str, level: str, sign_language: str, ui_language: str) -> str:

    url = sl_video_instructions_urls_kaltura[direction][level][sign_language]

    text_hide = button_texts[ui_language]["hide"]
    text_show = button_texts[ui_language]["show"]

    if level == "segment":
        template = SL_VIDEO_INSTRUCTIONS_TEMPLATE_SEGMENT_KALTURA
    else:
        template = SL_VIDEO_INSTRUCTIONS_TEMPLATE_DOCUMENT_KALTURA

    return template.format(url=url, text_hide=text_hide, text_show=text_show)


def get_sign_language_instructions(ui_language, text_to_sign, block_items, source_language, target_language,
                                   source_language_code, target_language_code, add_video_instructions: bool):

    source_language_correct_ui_language = language_names_per_ui_language[ui_language][source_language_code]
    target_language_correct_ui_language = language_names_per_ui_language[ui_language][target_language_code]

    if ui_language == "deu":
        if text_to_sign:
            priming_question_texts = [
                'Unten sehen Sie ein Dokument mit {0} Sätzen auf {1} (linke Spalten) '
                'und die entsprechenden möglichen Übersetzungen in {2} (rechte Spalten). Bewerten Sie jede mögliche '
                'Übersetzung des Satzes im Kontext des Dokuments. '
                'Sie können bereits bewertete Sätze jederzeit durch Anklicken eines '
                'Quelltextes erneut aufrufen und die Bewertung aktualisieren.'.format(
                    len(block_items) - 1,
                    source_language_correct_ui_language,
                    target_language_correct_ui_language,
                ),
            ]

        else:
            priming_question_texts = [
                'Unten sehen Sie ein Dokument mit {0} Sätzen in {1} (linke Spalten) und die entsprechenden möglichen '
                'Übersetzungen auf {2} (rechte Spalten). Bewerten Sie jede mögliche '
                'Übersetzung des Satzes im Kontext des Dokuments. '
                'Sie können bereits bewertete Sätze jederzeit durch Anklicken eines '
                'Eingabevideos erneut aufrufen und die Bewertung aktualisieren.'.format(
                    len(block_items) - 1,
                    source_language_correct_ui_language,
                    target_language_correct_ui_language,
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
                'Vous voyez ci-dessous un document avec {0} phrases en {1} (colonnes '
                'de gauche) et leurs traductions candidates correspondantes {2} (colonnes de droite). Veuillez attribuer un score '
                'à chaque traduction possible de la phrase dans le contexte du document. '
                'Vous pouvez revisiter les phrases déjà évaluées et mettre à jour leurs '
                'scores à tout moment en cliquant sur un texte source.'.format(
                    len(block_items) - 1,
                    source_language_correct_ui_language,
                    target_language_correct_ui_language,
                ),
            ]
        else:
            priming_question_texts = [
                'Vous voyez ci-dessous un document avec {0} phrases en {1} (colonnes de gauche) et leurs traductions candidates '
                'correspondantes en {2} (colonnes de droite). Veuillez attribuer un '
                'score à chaque traduction possible de la phrase dans le contexte du document. '
                'Vous pouvez revisiter les phrases déjà évaluées et mettre à jour leurs '
                'scores à tout moment en cliquant sur une vidéo source.'.format(
                    len(block_items) - 1,
                    source_language_correct_ui_language,
                    target_language_correct_ui_language,
                ),
            ]

        document_question_texts = [
            "Veuillez noter la qualité globale de la traduction du document (vous ne pouvez noter "
            "l'ensemble du document qu'après avoir noté toutes les phrases individuelles).",
        ]

    elif ui_language == "ita":
        if text_to_sign:
            priming_question_texts = [
                'Qui sotto trovate un documento con {0} frasi in {1} (colonne di sinistra) e le'
                'corrispondenti possibili traduzioni nella {2} (colonne di destra). Valutate '
                'ogni possibile traduzione della frase nel contesto del documento. Potete rivedere '
                'le frasi valutate in precedenza e aggiornarne le valutazioni in qualsiasi momento '
                'cliccando sul testo sorgente.'.format(
                    len(block_items) - 1,
                    source_language_correct_ui_language,
                    target_language_correct_ui_language,
                ),
            ]
        else:
            priming_question_texts = [
                'Qui sotto trovate un documento con {0} frasi nella {1} (colonne di sinistra) e le corrispondenti possibili traduzioni in '
                '{2} (colonne di destra). Valutate ogni possibile traduzione della '
                'frase nel contesto del documento. Potete rivedere le frasi valutate in '
                'precedenza e aggiornarne le valutazioni in qualsiasi momento cliccando '
                'su un video sorgente.'.format(
                    len(block_items) - 1,
                    source_language_correct_ui_language,
                    target_language_correct_ui_language,
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
                    source_language_correct_ui_language,
                    target_language_correct_ui_language,
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
                    source_language_correct_ui_language,
                    target_language_correct_ui_language,
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
