import mongoengine as me


class Review(me.Document):
    game_name = me.StringField(required=True)
    authors = me.StringField(required=True)

    player_experience_score = me.FloatField(required=True)
    mechanical_polish_score = me.FloatField(required=True)
    overall_gameplay_comments = me.StringField(required=True)

    theme_inclusion_score = me.FloatField(required=True)
    theme_inclusion_comments = me.StringField(required=True)

    general_presentation_score = me.FloatField(required=True)
    quality_graphics_score = me.FloatField(required=True)
    quality_audio_score = me.FloatField(required=True)
    overall_presentation_comments = me.StringField(required=True)

    penalties = me.ListField()

    final_comments = me.StringField()
    total_score = me.FloatField(required=True)
    video_review_link = me.StringField()
