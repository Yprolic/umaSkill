from peewee import *

database = SqliteDatabase('db/master.mdb')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AnnounceCharacter(BaseModel):
    can_end_second = IntegerField()
    movie_id = IntegerField()

    class Meta:
        table_name = 'announce_character'

class AnnounceData(BaseModel):
    announce_id = IntegerField()
    announce_type = IntegerField()
    end_date = IntegerField()
    priority = IntegerField()
    start_date = IntegerField()

    class Meta:
        table_name = 'announce_data'

class AnnounceSupportCard(BaseModel):
    cuts_pattern = IntegerField()
    support_card_id_a = IntegerField()
    support_card_id_b = IntegerField()
    support_card_id_c = IntegerField()
    type = IntegerField()

    class Meta:
        table_name = 'announce_support_card'

class AudioCuesheet(BaseModel):
    attribute = IntegerField(index=True)
    cue_sheet = TextField()

    class Meta:
        table_name = 'audio_cuesheet'

class AudioIgnoredCueOnHighspeed(BaseModel):
    cue_name = TextField()
    cue_sheet = TextField()

    class Meta:
        table_name = 'audio_ignored_cue_on_highspeed'
        indexes = (
            (('cue_name', 'cue_sheet'), False),
        )

class AvailableSkillSet(BaseModel):
    available_skill_set_id = IntegerField(index=True)
    need_rank = IntegerField()
    skill_id = IntegerField()

    class Meta:
        table_name = 'available_skill_set'

class BackgroundData(BaseModel):
    bg_id = IntegerField()
    bg_sub = IntegerField()
    bus_param_set_name = TextField()
    cue_name = TextField()
    height = IntegerField()
    pos_x = IntegerField()
    pos_y = IntegerField()
    sheet_name = TextField()
    width = IntegerField()

    class Meta:
        table_name = 'background_data'
        indexes = (
            (('bg_id', 'bg_sub'), True),
        )

class BannerData(BaseModel):
    banner_id = IntegerField()
    condition_value = IntegerField()
    end_date = TextField()
    group_id = IntegerField(index=True)
    priority = IntegerField()
    start_date = TextField()
    transition = IntegerField()
    type = IntegerField()

    class Meta:
        table_name = 'banner_data'

class CampaignCharaStorySchedule(BaseModel):
    campaign_id = IntegerField(index=True)
    chara_id = IntegerField(index=True)
    story_id = IntegerField()

    class Meta:
        table_name = 'campaign_chara_story_schedule'
        primary_key = False

class CampaignData(BaseModel):
    campaign_id = AutoField()
    effect_type_1 = IntegerField()
    effect_value_1 = IntegerField()
    end_time = IntegerField()
    image_icon_id = IntegerField()
    start_time = IntegerField()
    target_id = IntegerField()
    target_type = IntegerField(index=True)
    transition_type = IntegerField()
    user_show = IntegerField()

    class Meta:
        table_name = 'campaign_data'

class CardData(BaseModel):
    available_skill_set_id = IntegerField()
    bg_id = IntegerField()
    chara_id = IntegerField(index=True)
    default_rarity = IntegerField()
    get_piece_id = IntegerField(index=True)
    limited_chara = IntegerField()
    running_style = IntegerField()
    talent_group_id = IntegerField()
    talent_guts = IntegerField()
    talent_pow = IntegerField()
    talent_speed = IntegerField()
    talent_stamina = IntegerField()
    talent_wiz = IntegerField()

    class Meta:
        table_name = 'card_data'

class CardRarityData(BaseModel):
    card_id = IntegerField(index=True)
    get_dress_id_1 = IntegerField()
    get_dress_id_2 = IntegerField()
    guts = IntegerField()
    live_dress_id = IntegerField()
    max_guts = IntegerField()
    max_pow = IntegerField()
    max_speed = IntegerField()
    max_stamina = IntegerField()
    max_wiz = IntegerField()
    mini_dress_id = IntegerField()
    outgame_dress_id = IntegerField()
    pow = IntegerField()
    proper_distance_long = IntegerField()
    proper_distance_middle = IntegerField()
    proper_distance_mile = IntegerField()
    proper_distance_short = IntegerField()
    proper_ground_dirt = IntegerField()
    proper_ground_turf = IntegerField()
    proper_running_style_nige = IntegerField()
    proper_running_style_oikomi = IntegerField()
    proper_running_style_sashi = IntegerField()
    proper_running_style_senko = IntegerField()
    race_dress_id = IntegerField()
    rarity = IntegerField()
    skill_set = IntegerField()
    speed = IntegerField()
    stamina = IntegerField()
    wiz = IntegerField()

    class Meta:
        table_name = 'card_rarity_data'
        indexes = (
            (('card_id', 'rarity'), True),
        )

class CardTalentUpgrade(BaseModel):
    item_category_1 = IntegerField()
    item_category_2 = IntegerField()
    item_category_3 = IntegerField()
    item_category_4 = IntegerField()
    item_category_5 = IntegerField()
    item_category_6 = IntegerField()
    item_id_1 = IntegerField()
    item_id_2 = IntegerField()
    item_id_3 = IntegerField()
    item_id_4 = IntegerField()
    item_id_5 = IntegerField()
    item_id_6 = IntegerField()
    item_num_1 = IntegerField()
    item_num_2 = IntegerField()
    item_num_3 = IntegerField()
    item_num_4 = IntegerField()
    item_num_5 = IntegerField()
    item_num_6 = IntegerField()
    talent_group_id = IntegerField()
    talent_level = IntegerField()

    class Meta:
        table_name = 'card_talent_upgrade'
        indexes = (
            (('talent_group_id', 'talent_level'), False),
        )

class ChampionsBgm(BaseModel):
    cue_name = TextField()
    cuesheet_name = TextField()
    first_bgm_pattern = IntegerField()
    race_number = IntegerField()
    round_id = IntegerField()
    scene_type = IntegerField()
    second_bgm_pattern = IntegerField()

    class Meta:
        table_name = 'champions_bgm'
        indexes = (
            (('round_id', 'scene_type', 'race_number'), False),
        )

class ChampionsEvaluationRate(BaseModel):
    proper_rank = IntegerField()
    proper_type = IntegerField()
    rate = IntegerField()

    class Meta:
        table_name = 'champions_evaluation_rate'

class ChampionsNewsCharaComment(BaseModel):
    big_flag = IntegerField()
    chara_id = IntegerField()
    round_id = IntegerField(index=True)

    class Meta:
        table_name = 'champions_news_chara_comment'

class ChampionsNewsCharaDetail(BaseModel):
    chara_id = IntegerField()
    chara_text_group = IntegerField()
    nickname_id = IntegerField()
    parameter_min = IntegerField()
    parameter_type = IntegerField()
    proper_running_style_min = IntegerField()
    resource_id = IntegerField()
    running_style = IntegerField()
    single_win = IntegerField()
    text_number = IntegerField()

    class Meta:
        table_name = 'champions_news_chara_detail'

class ChampionsNewsCharaWininfo(BaseModel):
    chara_text_group = IntegerField()
    race_count_type = IntegerField()
    round_id = IntegerField()
    win_max = IntegerField()
    win_min = IntegerField()

    class Meta:
        table_name = 'champions_news_chara_wininfo'

class ChampionsNewsRace(BaseModel):
    resource_id = IntegerField()
    round_id = IntegerField(index=True)
    text_number = IntegerField()
    win_percent_type = IntegerField()

    class Meta:
        table_name = 'champions_news_race'

class ChampionsNewsTitle(BaseModel):
    resource_id = IntegerField()
    round_id = IntegerField(index=True)
    sub_title = IntegerField()
    title = IntegerField()
    win_percent_type = IntegerField()

    class Meta:
        table_name = 'champions_news_title'

class ChampionsNewsTrainerDetail(BaseModel):
    resource_id = IntegerField()
    text_number = IntegerField()
    trainer_text_group = IntegerField()

    class Meta:
        table_name = 'champions_news_trainer_detail'

class ChampionsNewsTrainerWininfo(BaseModel):
    race_count_type = IntegerField()
    round_id = IntegerField(index=True)
    trainer_text_group = IntegerField()
    win_max = IntegerField()
    win_min = IntegerField()

    class Meta:
        table_name = 'champions_news_trainer_wininfo'

class ChampionsRaceCondition(BaseModel):
    champions_id = IntegerField()
    race_condition_id = IntegerField()
    race_instance_id = IntegerField()
    round_id = IntegerField()

    class Meta:
        table_name = 'champions_race_condition'
        indexes = (
            (('champions_id', 'round_id'), True),
        )
        primary_key = CompositeKey('champions_id', 'round_id')

class ChampionsRewardRate(BaseModel):
    box_grade = IntegerField()
    champions_id = IntegerField()
    ranking = IntegerField()
    rate = IntegerField()
    reward_set_id = IntegerField()
    round_id = IntegerField()
    win_count = IntegerField()

    class Meta:
        table_name = 'champions_reward_rate'
        indexes = (
            (('champions_id', 'round_id'), False),
        )

class ChampionsRoundDetail(BaseModel):
    breakthrough_number_1 = IntegerField()
    breakthrough_number_2 = IntegerField()
    champions_id = IntegerField(index=True)
    entry_number = IntegerField()
    free_entry_number = IntegerField()
    round = IntegerField()
    round_id = IntegerField()
    round_number = IntegerField()
    tier = IntegerField()

    class Meta:
        table_name = 'champions_round_detail'
        indexes = (
            (('champions_id', 'round_id'), True),
        )
        primary_key = CompositeKey('champions_id', 'round_id')

class ChampionsRoundSchedule(BaseModel):
    champions_id = IntegerField(index=True)
    end_date = IntegerField()
    interval_end_time = IntegerField()
    interval_start_time = IntegerField()
    round = IntegerField()
    round_detail = IntegerField()
    start_date = IntegerField()

    class Meta:
        table_name = 'champions_round_schedule'

class ChampionsSchedule(BaseModel):
    champions_bg_id = IntegerField()
    champions_bg_position_x = IntegerField()
    champions_bg_sub_id = IntegerField()
    champions_finish_bg_id = IntegerField()
    champions_finish_bg_position_x = IntegerField()
    champions_finish_bg_sub_id = IntegerField()
    end_date = IntegerField()
    info_detail = IntegerField()
    notice_date = IntegerField()
    resource_id = IntegerField()
    start_date = IntegerField()

    class Meta:
        table_name = 'champions_schedule'

class ChampionsStandMotion(BaseModel):
    chara_id = IntegerField()
    motion_set = IntegerField()
    race_dress_id = IntegerField()
    type = IntegerField()

    class Meta:
        table_name = 'champions_stand_motion'
        indexes = (
            (('chara_id', 'type'), True),
        )
        primary_key = CompositeKey('chara_id', 'type')

class CharaCategoryMotion(BaseModel):
    chara_id = AutoField()
    standby_motion_1 = IntegerField()
    standby_motion_2 = IntegerField()
    standby_motion_3 = IntegerField()
    standby_motion_4 = IntegerField()
    standby_motion_5 = IntegerField()
    standby_motion_6 = IntegerField()

    class Meta:
        table_name = 'chara_category_motion'

class CharaData(BaseModel):
    attachment_model_id = IntegerField()
    birth_day = IntegerField()
    birth_month = IntegerField()
    birth_year = IntegerField()
    bust = IntegerField()
    chara_category = IntegerField()
    ear_random_time_max = IntegerField()
    ear_random_time_min = IntegerField()
    height = IntegerField()
    image_color_main = TextField()
    image_color_sub = TextField()
    mini_mayu_shader_type = IntegerField()
    personal_dress = IntegerField()
    race_running_type = IntegerField()
    scale = IntegerField()
    sex = IntegerField()
    shape = IntegerField()
    skin = IntegerField()
    socks = IntegerField()
    start_date = IntegerField()
    story_ear_random_time_max = IntegerField()
    story_ear_random_time_min = IntegerField()
    story_tail_random_time_max = IntegerField()
    story_tail_random_time_min = IntegerField()
    tail_model_id = IntegerField()
    tail_random_time_max = IntegerField()
    tail_random_time_min = IntegerField()
    ui_border_color = TextField()
    ui_color_main = TextField()
    ui_color_sub = TextField()
    ui_nameplate_color_1 = TextField()
    ui_nameplate_color_2 = TextField()
    ui_num_color_1 = TextField()
    ui_num_color_2 = TextField()
    ui_speech_color_1 = TextField()
    ui_speech_color_2 = TextField()
    ui_training_color_1 = TextField()
    ui_training_color_2 = TextField()
    ui_turn_color = TextField()
    ui_wipe_color_1 = TextField()
    ui_wipe_color_2 = TextField()
    ui_wipe_color_3 = TextField()

    class Meta:
        table_name = 'chara_data'

class CharaMotionAct(BaseModel):
    chara_id = IntegerField(index=True)
    command_name = TextField()
    target_motion = IntegerField()

    class Meta:
        table_name = 'chara_motion_act'
        indexes = (
            (('chara_id', 'command_name'), True),
        )

class CharaMotionSet(BaseModel):
    body_motion = TextField()
    body_motion_play_type = IntegerField()
    body_motion_type = IntegerField()
    cheek = IntegerField()
    ear_motion = TextField()
    eye_default = IntegerField()
    face_type = TextField()
    tail_motion = TextField()
    tail_motion_type = IntegerField()

    class Meta:
        table_name = 'chara_motion_set'

class CharaStoryData(BaseModel):
    add_reward_category_1 = IntegerField()
    add_reward_id_1 = IntegerField()
    add_reward_num_1 = IntegerField()
    chara_id = IntegerField(index=True)
    episode_index = IntegerField()
    exp_type = IntegerField()
    lock_type_1 = IntegerField()
    lock_value_1_1 = IntegerField()
    lock_value_1_2 = IntegerField()
    story_id = IntegerField(unique=True)

    class Meta:
        table_name = 'chara_story_data'
        indexes = (
            (('chara_id', 'episode_index'), False),
        )

class CharaType(BaseModel):
    chara_id = IntegerField()
    id = TextField(primary_key=True)
    target_cut = IntegerField()
    target_scene = IntegerField()
    target_type = IntegerField()
    value = IntegerField()

    class Meta:
        table_name = 'chara_type'
        indexes = (
            (('target_scene', 'target_cut'), False),
        )

class CharacterPropAnimation(BaseModel):
    layer_index = IntegerField()
    prop_anim_id = IntegerField()
    prop_id = IntegerField()
    scene_type = IntegerField()
    use_state_name = TextField()

    class Meta:
        table_name = 'character_prop_animation'
        indexes = (
            (('prop_id', 'scene_type'), False),
        )

class CharacterSystemLottery(BaseModel):
    card_id = IntegerField()
    card_rarity_id = IntegerField()
    chara_id = IntegerField(index=True)
    param1 = IntegerField()
    per = IntegerField()
    priority = IntegerField()
    sys_text_id = IntegerField()
    trigger = IntegerField()

    class Meta:
        table_name = 'character_system_lottery'
        indexes = (
            (('chara_id', 'trigger'), False),
            (('trigger', 'param1'), False),
        )

class CharacterSystemText(BaseModel):
    card_id = IntegerField()
    character_id = IntegerField(index=True)
    cue_id = IntegerField()
    cue_sheet = TextField()
    gender = IntegerField()
    lip_sync_data = TextField()
    motion_second_set = IntegerField()
    motion_second_start = IntegerField()
    motion_set = IntegerField()
    scene = IntegerField()
    text = TextField()
    use_gallery = IntegerField()
    voice_id = IntegerField()

    class Meta:
        table_name = 'character_system_text'
        indexes = (
            (('character_id', 'voice_id'), True),
        )
        primary_key = CompositeKey('character_id', 'voice_id')

class CircleRankData(BaseModel):
    need_ranking_max = IntegerField()
    need_ranking_min = IntegerField()
    reward_item_category_1 = IntegerField()
    reward_item_category_2 = IntegerField()
    reward_item_id_1 = IntegerField()
    reward_item_id_2 = IntegerField()
    reward_num_1 = IntegerField()
    reward_num_2 = IntegerField()

    class Meta:
        table_name = 'circle_rank_data'

class CircleStampData(BaseModel):
    disp_order = IntegerField(unique=True)
    start_date = TextField()

    class Meta:
        table_name = 'circle_stamp_data'

class CraneGameArmSwing(BaseModel):
    odds_1 = IntegerField()
    odds_2 = IntegerField()
    odds_3 = IntegerField()
    result_type = AutoField()

    class Meta:
        table_name = 'crane_game_arm_swing'

class CraneGameCatchResult(BaseModel):
    get_num = IntegerField()
    lottery_weight_1_1 = IntegerField()
    lottery_weight_1_2 = IntegerField()
    lottery_weight_2_1 = IntegerField()
    lottery_weight_2_2 = IntegerField()
    lottery_weight_3_1 = IntegerField()
    lottery_weight_3_2 = IntegerField()
    lottery_weight_extra_1 = IntegerField()
    lottery_weight_extra_2 = IntegerField()
    odds_id = IntegerField()

    class Meta:
        table_name = 'crane_game_catch_result'
        indexes = (
            (('odds_id', 'get_num'), True),
        )
        primary_key = CompositeKey('get_num', 'odds_id')

class CraneGameDefineParam(BaseModel):
    distance1 = TextField()
    distance2 = TextField()
    move_speed_1 = TextField()
    move_speed_2 = TextField()
    move_speed_3 = TextField()

    class Meta:
        table_name = 'crane_game_define_param'

class CraneGameExtraOddsCondition(BaseModel):
    credit = AutoField()
    get_num = IntegerField()

    class Meta:
        table_name = 'crane_game_extra_odds_condition'

class CraneGameHiddenOdds(BaseModel):
    animation_id = IntegerField()
    big = IntegerField()
    big_index = IntegerField()
    crane_animation_id = IntegerField()
    joint_type = IntegerField()
    lift_type = IntegerField()
    num = IntegerField()
    odds_1 = IntegerField()
    odds_2 = IntegerField()
    odds_3 = IntegerField()
    odds_extra = IntegerField()
    push_type = IntegerField()
    rare_effect_odds = IntegerField()
    type_id = IntegerField()

    class Meta:
        table_name = 'crane_game_hidden_odds'

class CraneGamePrizeFace(BaseModel):
    face_type = TextField()

    class Meta:
        table_name = 'crane_game_prize_face'

class CraneGamePrizePattern(BaseModel):
    prop_pattern_id = IntegerField()

    class Meta:
        table_name = 'crane_game_prize_pattern'

class CraneGameProp(BaseModel):
    num = IntegerField()
    type = AutoField()

    class Meta:
        table_name = 'crane_game_prop'

class DailyPack(BaseModel):
    daily_free_num = IntegerField()
    end_date = TextField()
    group_id = IntegerField(index=True)
    platform_id = IntegerField()
    repurchase_day = IntegerField()
    shop_data_id = IntegerField()
    start_date = TextField()
    term = IntegerField()

    class Meta:
        table_name = 'daily_pack'
        indexes = (
            (('shop_data_id', 'platform_id'), True),
        )
        primary_key = CompositeKey('platform_id', 'shop_data_id')

class DailyRace(BaseModel):
    cost_num = IntegerField()
    difficulty = IntegerField()
    end_date = IntegerField()
    first_clear_item_category_1 = IntegerField()
    first_clear_item_category_2 = IntegerField()
    first_clear_item_category_3 = IntegerField()
    first_clear_item_id_1 = IntegerField()
    first_clear_item_id_2 = IntegerField()
    first_clear_item_id_3 = IntegerField()
    first_clear_item_num_1 = IntegerField()
    first_clear_item_num_2 = IntegerField()
    first_clear_item_num_3 = IntegerField()
    group_id = IntegerField()
    normal_rewards_odds_id = IntegerField()
    pick_up_item_category_1 = IntegerField()
    pick_up_item_category_2 = IntegerField()
    pick_up_item_category_3 = IntegerField()
    pick_up_item_id_1 = IntegerField()
    pick_up_item_id_2 = IntegerField()
    pick_up_item_id_3 = IntegerField()
    pick_up_item_num_1 = IntegerField()
    pick_up_item_num_2 = IntegerField()
    pick_up_item_num_3 = IntegerField()
    race_instance_id = IntegerField(index=True)
    rare_reward_odds_id = IntegerField()
    start_date = IntegerField()
    unique_chara_npc_max = IntegerField()
    unique_chara_npc_min = IntegerField()

    class Meta:
        table_name = 'daily_race'

class DailyRaceBilling(BaseModel):
    frequency = IntegerField()
    pay_cost = IntegerField()

    class Meta:
        table_name = 'daily_race_billing'

class DailyRaceNpc(BaseModel):
    chara_id = IntegerField()
    guts = IntegerField()
    mob_id = IntegerField()
    npc_group_id = IntegerField()
    pow = IntegerField()
    proper_distance_long = IntegerField()
    proper_distance_middle = IntegerField()
    proper_distance_mile = IntegerField()
    proper_distance_short = IntegerField()
    proper_ground_dirt = IntegerField()
    proper_ground_turf = IntegerField()
    proper_running_style_nige = IntegerField()
    proper_running_style_oikomi = IntegerField()
    proper_running_style_sashi = IntegerField()
    proper_running_style_senko = IntegerField()
    race_dress_id = IntegerField()
    race_instance_id = IntegerField()
    skill_set_id = IntegerField()
    speed = IntegerField()
    stamina = IntegerField()
    wiz = IntegerField()

    class Meta:
        table_name = 'daily_race_npc'

class Directory(BaseModel):
    item_category_1 = IntegerField()
    item_id_1 = IntegerField()
    item_num_1 = IntegerField()
    rank_level = IntegerField(unique=True)
    required_point = IntegerField(index=True)

    class Meta:
        table_name = 'directory'

class DressData(BaseModel):
    body_setting = IntegerField()
    body_type = IntegerField(index=True)
    body_type_sub = IntegerField()
    chara_id = IntegerField(index=True)
    color_num = IntegerField()
    condition_type = IntegerField(index=True)
    disp_order = IntegerField()
    dress_color_main = TextField()
    dress_color_sub = TextField()
    end_time = IntegerField()
    have_mini = IntegerField()
    head_sub_id = IntegerField()
    is_dirt = IntegerField()
    is_wet = IntegerField()
    start_time = IntegerField()
    tail_model_id = IntegerField()
    tail_model_sub_id = IntegerField()
    use_gender = IntegerField()
    use_home = IntegerField()
    use_live = IntegerField()
    use_live_theater = IntegerField()
    use_race = IntegerField()
    use_season = IntegerField()

    class Meta:
        table_name = 'dress_data'

class EventMotionData(BaseModel):
    base_state_name = TextField()
    category = IntegerField()
    command_name = TextField()
    end_blend_time = IntegerField()
    pose_blend = IntegerField()
    start_blend_time = IntegerField()
    state_group = IntegerField()
    type = IntegerField(index=True)

    class Meta:
        table_name = 'event_motion_data'

class EventMotionPlusData(BaseModel):
    base_state_name = TextField(index=True)
    command_name = TextField()
    end_blend_time = IntegerField()
    layer_index = IntegerField(index=True)
    start_blend_time = IntegerField()
    tail_motion_type = IntegerField()

    class Meta:
        table_name = 'event_motion_plus_data'

class FaceTypeData(BaseModel):
    eye_l = TextField()
    eye_r = TextField()
    eyebrow_l = TextField()
    eyebrow_r = TextField()
    inverce_face_type = TextField()
    label = TextField(primary_key=True)
    mouth = TextField()
    mouth_shape_type = IntegerField()
    set_face_group = IntegerField()

    class Meta:
        table_name = 'face_type_data'

class FacialMouthChange(BaseModel):
    after_facialname = TextField()
    before_facialname = TextField()
    chara_id = IntegerField(index=True)

    class Meta:
        table_name = 'facial_mouth_change'
        indexes = (
            (('chara_id', 'before_facialname'), True),
        )

class GachaAvailable(BaseModel):
    card_id = IntegerField()
    card_type = IntegerField()
    gacha_id = IntegerField(index=True)
    is_pickup = IntegerField()
    is_prize_selectable = IntegerField()
    odds = IntegerField()
    rarity = IntegerField()
    recommend_order = IntegerField()

    class Meta:
        table_name = 'gacha_available'
        indexes = (
            (('gacha_id', 'card_id'), True),
        )
        primary_key = CompositeKey('card_id', 'gacha_id')

class GachaData(BaseModel):
    additional_piece_num_1 = IntegerField()
    additional_piece_num_2 = IntegerField()
    additional_piece_num_3 = IntegerField()
    additional_piece_num_4 = IntegerField()
    additional_piece_num_5 = IntegerField()
    additional_piece_num_6 = IntegerField()
    additional_piece_target_card_id_1 = IntegerField()
    additional_piece_target_card_id_2 = IntegerField()
    additional_piece_target_card_id_3 = IntegerField()
    additional_piece_target_card_id_4 = IntegerField()
    additional_piece_target_card_id_5 = IntegerField()
    additional_piece_target_card_id_6 = IntegerField()
    additional_piece_target_card_type_1 = IntegerField()
    additional_piece_target_card_type_2 = IntegerField()
    additional_piece_target_card_type_3 = IntegerField()
    additional_piece_target_card_type_4 = IntegerField()
    additional_piece_target_card_type_5 = IntegerField()
    additional_piece_target_card_type_6 = IntegerField()
    additional_piece_target_rarity_1 = IntegerField()
    additional_piece_target_rarity_2 = IntegerField()
    additional_piece_target_rarity_3 = IntegerField()
    additional_piece_target_rarity_4 = IntegerField()
    additional_piece_target_rarity_5 = IntegerField()
    additional_piece_target_rarity_6 = IntegerField()
    bonus_item_category_1 = IntegerField()
    bonus_item_category_2 = IntegerField()
    bonus_item_id_1 = IntegerField()
    bonus_item_id_2 = IntegerField()
    bonus_item_num_1 = IntegerField()
    bonus_item_num_2 = IntegerField()
    bonus_target_draw_num = IntegerField()
    card_type = IntegerField()
    cost_single = IntegerField()
    cost_type = IntegerField()
    daily_pay_cost = IntegerField()
    disp_order = IntegerField()
    draw_guarantee_num = IntegerField()
    draw_guarantee_rarity = IntegerField()
    end_date = IntegerField()
    only_once_flag = IntegerField()
    prize_odds_id = IntegerField()
    rarity_odds_id = IntegerField()
    start_date = IntegerField()
    type = IntegerField()

    class Meta:
        table_name = 'gacha_data'

class GachaExchange(BaseModel):
    card_id = IntegerField()
    card_type = IntegerField()
    gacha_id = IntegerField(index=True)
    pay_item_num = IntegerField()

    class Meta:
        table_name = 'gacha_exchange'
        indexes = (
            (('gacha_id', 'card_id'), True),
        )
        primary_key = CompositeKey('card_id', 'gacha_id')

class GachaFreeCampaign(BaseModel):
    end_date = IntegerField()
    gacha_id = IntegerField()
    start_date = IntegerField()
    target_draw_type = IntegerField()

    class Meta:
        table_name = 'gacha_free_campaign'

class GachaPiece(BaseModel):
    item_category = IntegerField()
    item_id = IntegerField()
    piece_num = IntegerField()
    piece_type = IntegerField()
    rarity = IntegerField(index=True)

    class Meta:
        table_name = 'gacha_piece'

class GachaPrizeOdds(BaseModel):
    item_category_1 = IntegerField()
    item_category_2 = IntegerField()
    item_category_3 = IntegerField()
    item_category_4 = IntegerField()
    item_category_5 = IntegerField()
    item_category_6 = IntegerField()
    item_id_1 = IntegerField()
    item_id_2 = IntegerField()
    item_id_3 = IntegerField()
    item_id_4 = IntegerField()
    item_id_5 = IntegerField()
    item_id_6 = IntegerField()
    item_num_1 = IntegerField()
    item_num_2 = IntegerField()
    item_num_3 = IntegerField()
    item_num_4 = IntegerField()
    item_num_5 = IntegerField()
    item_num_6 = IntegerField()
    odds = IntegerField()
    piece_num = IntegerField()
    place = IntegerField()
    prize_odds_id = IntegerField(index=True)

    class Meta:
        table_name = 'gacha_prize_odds'
        indexes = (
            (('prize_odds_id', 'place'), True),
        )
        primary_key = CompositeKey('place', 'prize_odds_id')

class GachaTopBg(BaseModel):
    gacha_id = IntegerField(index=True)

    class Meta:
        table_name = 'gacha_top_bg'

class GiftMessage(BaseModel):
    type_1 = IntegerField()
    type_2 = IntegerField()
    type_3 = IntegerField()
    type_4 = IntegerField()

    class Meta:
        table_name = 'gift_message'

class HighlightInterpolate(BaseModel):
    in_time = IntegerField()
    out_time = IntegerField()

    class Meta:
        table_name = 'highlight_interpolate'

class HomeCharacterType(BaseModel):
    change_personality = IntegerField()
    original_personality = IntegerField()
    pos_id = IntegerField()

    class Meta:
        table_name = 'home_character_type'
        indexes = (
            (('pos_id', 'original_personality'), True),
        )
        primary_key = CompositeKey('original_personality', 'pos_id')

class HomeEnvSetting(BaseModel):
    bgm_cue_name = TextField()
    bgm_cuesheet_name = TextField()
    env_cue_name = TextField()
    env_cuesheet_name = TextField()
    home_event_type = IntegerField()
    home_set_id = IntegerField()
    resource = IntegerField()
    resource_event_check = IntegerField()
    season = IntegerField()
    timezone = IntegerField()
    weather = IntegerField()

    class Meta:
        table_name = 'home_env_setting'
        indexes = (
            (('home_set_id', 'home_event_type', 'season', 'weather', 'timezone'), True),
        )

class HomePosterData(BaseModel):
    detail_value = IntegerField()
    end_date = IntegerField()
    height = IntegerField()
    posi_horizontal = IntegerField()
    posi_vertical = IntegerField()
    priority = IntegerField(index=True)
    start_date = IntegerField()
    url = TextField()
    url_value = IntegerField()
    width = IntegerField()

    class Meta:
        table_name = 'home_poster_data'

class HomePropSetting(BaseModel):
    attach_node = IntegerField()
    personality = IntegerField()
    pos_id = IntegerField()
    prop_id = IntegerField()

    class Meta:
        table_name = 'home_prop_setting'
        indexes = (
            (('pos_id', 'personality'), True),
        )
        primary_key = CompositeKey('personality', 'pos_id')

class HomeStoryTrigger(BaseModel):
    chara_id_1 = IntegerField()
    chara_id_2 = IntegerField()
    chara_id_3 = IntegerField()
    condition_type = IntegerField()
    home_event_type = IntegerField()
    num = IntegerField()
    pos_id = IntegerField(index=True)
    story_id = IntegerField()

    class Meta:
        table_name = 'home_story_trigger'
        indexes = (
            (('home_event_type', 'story_id'), False),
        )

class HomeWalkGroup(BaseModel):
    chara_id_1 = IntegerField()
    chara_id_2 = IntegerField()
    chara_id_3 = IntegerField()

    class Meta:
        table_name = 'home_walk_group'

class HonorData(BaseModel):
    category = IntegerField()
    condition_type = IntegerField()
    condition_value = IntegerField()
    condition_value_2 = IntegerField()
    end_date = TextField()
    rank = IntegerField()
    start_date = TextField()
    step_group_id = IntegerField()
    step_order = IntegerField()

    class Meta:
        table_name = 'honor_data'

class ItemData(BaseModel):
    add_value_1 = IntegerField()
    add_value_2 = IntegerField()
    add_value_3 = IntegerField()
    effect_target_1 = IntegerField()
    effect_target_2 = IntegerField()
    effect_type_1 = IntegerField()
    effect_type_2 = IntegerField()
    effect_value_1 = IntegerField()
    effect_value_2 = IntegerField()
    enable_request = IntegerField()
    end_date = TextField()
    group_id = IntegerField(index=True)
    item_category = IntegerField(index=True)
    item_place_id = IntegerField()
    limit_num = IntegerField()
    rare = IntegerField()
    request_reward = IntegerField()
    sort = IntegerField()
    start_date = TextField()

    class Meta:
        table_name = 'item_data'

class ItemExchange(BaseModel):
    additional_piece_num = IntegerField()
    change_item_category = IntegerField()
    change_item_id = IntegerField()
    change_item_limit_num = IntegerField()
    change_item_limit_type = IntegerField()
    change_item_num = IntegerField()
    condition_type = IntegerField()
    condition_value_1 = IntegerField()
    condition_value_2 = IntegerField()
    disp_order = IntegerField()
    end_date = IntegerField()
    item_exchange_top_id = IntegerField(index=True)
    pay_item_category = IntegerField()
    pay_item_id = IntegerField(index=True)
    pay_item_num = IntegerField()
    price_change_group_id = IntegerField()
    start_date = IntegerField()

    class Meta:
        table_name = 'item_exchange'

class ItemExchangeTop(BaseModel):
    item_exchange_disp_order = IntegerField()

    class Meta:
        table_name = 'item_exchange_top'

class ItemGroup(BaseModel):
    group_id = IntegerField(index=True)

    class Meta:
        table_name = 'item_group'

class ItemPack(BaseModel):
    end_date = TextField()
    item_category = IntegerField()
    item_id = IntegerField()
    item_num = IntegerField()
    item_pack_id = IntegerField()
    start_date = TextField()

    class Meta:
        table_name = 'item_pack'

class ItemPlace(BaseModel):
    id = IntegerField(index=True)
    transition_type = IntegerField()
    transition_value = IntegerField()

    class Meta:
        table_name = 'item_place'
        indexes = (
            (('id', 'transition_type', 'transition_value'), True),
        )
        primary_key = False

class LegendRace(BaseModel):
    cost_num = IntegerField()
    difficulty = IntegerField()
    drop_reward_odds_id = IntegerField()
    end_date = IntegerField()
    first_clear_item_category_1 = IntegerField()
    first_clear_item_category_2 = IntegerField()
    first_clear_item_category_3 = IntegerField()
    first_clear_item_id_1 = IntegerField()
    first_clear_item_id_2 = IntegerField()
    first_clear_item_id_3 = IntegerField()
    first_clear_item_num_1 = IntegerField()
    first_clear_item_num_2 = IntegerField()
    first_clear_item_num_3 = IntegerField()
    ground = IntegerField()
    group_id = IntegerField(index=True)
    image_id = IntegerField()
    legend_bg_id = IntegerField()
    legend_bg_sub_id = IntegerField()
    legend_race_boss_npc_id = IntegerField()
    pick_up_item_category_1 = IntegerField()
    pick_up_item_category_2 = IntegerField()
    pick_up_item_category_3 = IntegerField()
    pick_up_item_id_1 = IntegerField()
    pick_up_item_id_2 = IntegerField()
    pick_up_item_id_3 = IntegerField()
    pick_up_item_num_1 = IntegerField()
    pick_up_item_num_2 = IntegerField()
    pick_up_item_num_3 = IntegerField()
    race_instance_id = IntegerField(index=True)
    season = IntegerField()
    start_date = IntegerField()
    victory_reward_odds_id = IntegerField()
    weather = IntegerField()

    class Meta:
        table_name = 'legend_race'

class LegendRaceBilling(BaseModel):
    frequency = IntegerField()
    pay_cost = IntegerField()

    class Meta:
        table_name = 'legend_race_billing'

class LegendRaceBossNpc(BaseModel):
    card_rarity_data_id = IntegerField()
    chara_id = IntegerField()
    guts = IntegerField()
    nickname_id = IntegerField()
    pow = IntegerField()
    proper_distance_long = IntegerField()
    proper_distance_middle = IntegerField()
    proper_distance_mile = IntegerField()
    proper_distance_short = IntegerField()
    proper_ground_dirt = IntegerField()
    proper_ground_turf = IntegerField()
    proper_running_style_nige = IntegerField()
    proper_running_style_oikomi = IntegerField()
    proper_running_style_sashi = IntegerField()
    proper_running_style_senko = IntegerField()
    race_dress_id = IntegerField()
    skill_set_id = IntegerField()
    speed = IntegerField()
    stamina = IntegerField()
    wiz = IntegerField()

    class Meta:
        table_name = 'legend_race_boss_npc'

class LegendRaceNpc(BaseModel):
    chara_id = IntegerField()
    guts = IntegerField()
    mob_id = IntegerField()
    npc_group_id = IntegerField()
    pow = IntegerField()
    proper_distance_long = IntegerField()
    proper_distance_middle = IntegerField()
    proper_distance_mile = IntegerField()
    proper_distance_short = IntegerField()
    proper_ground_dirt = IntegerField()
    proper_ground_turf = IntegerField()
    proper_running_style_nige = IntegerField()
    proper_running_style_oikomi = IntegerField()
    proper_running_style_sashi = IntegerField()
    proper_running_style_senko = IntegerField()
    race_dress_id = IntegerField()
    race_instance_id = IntegerField()
    skill_set_id = IntegerField()
    speed = IntegerField()
    stamina = IntegerField()
    wiz = IntegerField()

    class Meta:
        table_name = 'legend_race_npc'

class LimitedExchange(BaseModel):
    daily_race_ceiling = IntegerField()
    daily_race_odds = IntegerField()
    end_date = IntegerField()
    item_exchange_top_id = IntegerField()
    item_lineup_value = IntegerField()
    legend_race_ceiling = IntegerField()
    legend_race_odds = IntegerField()
    odds_id = IntegerField()
    open_value = IntegerField()
    single_mode_ceiling = IntegerField()
    single_mode_odds = IntegerField()
    start_date = IntegerField()
    team_stadium_ceiling = IntegerField()
    team_stadium_odds = IntegerField()

    class Meta:
        table_name = 'limited_exchange'

class LimitedExchangeReward(BaseModel):
    group_id = IntegerField()
    item_exchange_id = IntegerField()
    odds = IntegerField()
    ribbon_value = IntegerField()

    class Meta:
        table_name = 'limited_exchange_reward'

class LimitedExchangeRewardOdds(BaseModel):
    disp_order = IntegerField()
    group_id = IntegerField()
    odds = IntegerField()
    odds_id = IntegerField()

    class Meta:
        table_name = 'limited_exchange_reward_odds'

class LiveData(BaseModel):
    backdancer_dress = IntegerField()
    backdancer_dress_color = IntegerField()
    backdancer_order = IntegerField()
    condition_type = IntegerField()
    default_main_dress = IntegerField()
    default_main_dress_color = IntegerField()
    default_mob_dress = IntegerField()
    default_mob_dress_color = IntegerField()
    end_date = IntegerField()
    live_member_number = IntegerField()
    music_id = AutoField()
    music_type = IntegerField()
    song_chara_type = IntegerField()
    sort = IntegerField(unique=True)
    start_date = IntegerField()
    title_color_bottom = TextField()
    title_color_top = TextField()

    class Meta:
        table_name = 'live_data'

class LivePermissionData(BaseModel):
    chara_id = IntegerField()
    music_id = IntegerField(index=True)

    class Meta:
        table_name = 'live_permission_data'
        indexes = (
            (('music_id', 'chara_id'), True),
        )
        primary_key = CompositeKey('chara_id', 'music_id')

class LoginBonusData(BaseModel):
    count_num = IntegerField()
    disp_order = IntegerField(unique=True)
    end_date = TextField()
    start_date = TextField()
    type = IntegerField(index=True)

    class Meta:
        table_name = 'login_bonus_data'

class LoginBonusDetail(BaseModel):
    count = IntegerField()
    item_category = IntegerField()
    item_id = IntegerField()
    item_num = IntegerField()
    login_bonus_id = IntegerField(index=True)

    class Meta:
        table_name = 'login_bonus_detail'
        indexes = (
            (('login_bonus_id', 'count'), True),
        )

class LoveRank(BaseModel):
    rank = IntegerField(unique=True)
    total_point = IntegerField()

    class Meta:
        table_name = 'love_rank'

class MainStoryData(BaseModel):
    add_reward_category_1 = IntegerField()
    add_reward_id_1 = IntegerField()
    add_reward_num_1 = IntegerField()
    episode_index = IntegerField()
    lock_type_1 = IntegerField()
    lock_type_2 = IntegerField()
    lock_type_3 = IntegerField()
    lock_value_1_1 = IntegerField()
    lock_value_1_2 = IntegerField()
    lock_value_2_1 = IntegerField()
    lock_value_2_2 = IntegerField()
    lock_value_3_1 = IntegerField()
    lock_value_3_2 = IntegerField()
    part_id = IntegerField(index=True)
    story_id_1 = IntegerField(unique=True)
    story_id_2 = IntegerField()
    story_id_3 = IntegerField()
    story_id_4 = IntegerField()
    story_id_5 = IntegerField()
    story_number = IntegerField()
    story_type_1 = IntegerField()
    story_type_2 = IntegerField()
    story_type_3 = IntegerField()
    story_type_4 = IntegerField()
    story_type_5 = IntegerField()

    class Meta:
        table_name = 'main_story_data'

class MainStoryPart(BaseModel):
    main_story_last_chapter = IntegerField()
    start_date = IntegerField()
    ui_color = TextField()

    class Meta:
        table_name = 'main_story_part'

class MainStoryRaceCharaData(BaseModel):
    bracket_number = IntegerField()
    chara_id = IntegerField()
    dress_id = IntegerField()
    group_id = IntegerField(index=True)
    guts = IntegerField()
    mob_id = IntegerField()
    motivation = IntegerField()
    pow = IntegerField()
    proper_distance_long = IntegerField()
    proper_distance_middle = IntegerField()
    proper_distance_mile = IntegerField()
    proper_distance_short = IntegerField()
    proper_ground_dirt = IntegerField()
    proper_ground_turf = IntegerField()
    proper_running_style_nige = IntegerField()
    proper_running_style_oikomi = IntegerField()
    proper_running_style_sashi = IntegerField()
    proper_running_style_senko = IntegerField()
    running_style = IntegerField()
    skill_set_id = IntegerField()
    speed = IntegerField()
    stamina = IntegerField()
    wiz = IntegerField()

    class Meta:
        table_name = 'main_story_race_chara_data'

class MainStoryRaceData(BaseModel):
    bonus_chara_1 = IntegerField()
    bonus_chara_2 = IntegerField()
    bonus_chara_3 = IntegerField()
    clear_rank = IntegerField()
    group_id = IntegerField()
    race_condition_id = IntegerField()
    race_instance_id = IntegerField()

    class Meta:
        table_name = 'main_story_race_data'

class MiniBg(BaseModel):
    dress_id = IntegerField()
    grid_offset_x = TextField()
    grid_offset_y = TextField()
    position = TextField()
    release_num = IntegerField()
    scene_type = IntegerField(index=True)
    size_x = IntegerField()
    size_y = IntegerField()

    class Meta:
        table_name = 'mini_bg'

class MiniBgCharaMotion(BaseModel):
    bg_id = IntegerField(index=True)
    chara_pos_y = TextField()
    chara_shadow = IntegerField()
    direction = IntegerField()
    effect_id = IntegerField()
    effect_start_sec = TextField()
    fixed_render_order = IntegerField()
    grid_pos_x = IntegerField()
    grid_pos_y = IntegerField()
    group_id = IntegerField()
    is_mob = IntegerField()
    main_chara_num = IntegerField()
    motion_name = TextField()
    pos_obj = TextField()
    position_anim = TextField()
    position_file = TextField()
    priority = IntegerField()
    se_cue_name01 = TextField()
    se_cue_name02 = TextField()
    se_cue_sheet01 = TextField()
    se_cue_sheet02 = TextField()
    se_start_frame01 = IntegerField()
    se_start_frame02 = IntegerField()
    sub_group_id = IntegerField()
    timeline = TextField()
    timeline_actor = TextField()
    use_grid_pos_job_select = IntegerField()

    class Meta:
        table_name = 'mini_bg_chara_motion'

class MiniFaceTypeData(BaseModel):
    cheek = IntegerField()
    eye_l = IntegerField()
    eye_r = IntegerField()
    eyebrow_l = IntegerField()
    eyebrow_r = IntegerField()
    label = TextField(primary_key=True)
    mouth = IntegerField()

    class Meta:
        table_name = 'mini_face_type_data'

class MiniMotionSet(BaseModel):
    add_layer_index = IntegerField()
    body_motion = TextField()
    body_motion_play_type = IntegerField()
    body_motion_scene_type = IntegerField()
    body_motion_type = IntegerField()
    chara_face_type = TextField()
    chara_type_target = IntegerField()
    ear_motion = TextField()
    facial_motion = TextField()
    id = IntegerField(index=True)
    is_enable_randome_ear = IntegerField()
    is_enable_randome_tail = IntegerField()
    is_mirror = IntegerField()
    is_prop_require_motion_end = IntegerField()
    label = TextField(primary_key=True)
    prop_attach_node_name_type = IntegerField()
    prop_id = IntegerField()
    prop_motion = TextField()
    prop_motion_scene_type = IntegerField()
    scene_sub_folder = TextField()
    tail_motion = TextField()
    tail_motion_type = IntegerField()
    transition_time = IntegerField()

    class Meta:
        table_name = 'mini_motion_set'

class MiniMouthType(BaseModel):
    reverse_mouth_id = IntegerField()
    type = IntegerField()

    class Meta:
        table_name = 'mini_mouth_type'

class MissionData(BaseModel):
    condition_num = IntegerField()
    condition_type = IntegerField()
    condition_value_1 = IntegerField()
    condition_value_2 = IntegerField()
    condition_value_3 = IntegerField()
    condition_value_4 = IntegerField()
    date_check_flg = IntegerField()
    disp_order = IntegerField()
    end_date = TextField()
    event_id = IntegerField()
    item_category = IntegerField()
    item_id = IntegerField()
    item_num = IntegerField()
    mission_type = IntegerField(index=True)
    start_date = TextField()
    step_group_id = IntegerField()
    step_order = IntegerField()
    transition_type = IntegerField()

    class Meta:
        table_name = 'mission_data'

class MobData(BaseModel):
    attachment_model_id = IntegerField()
    capture_type = IntegerField()
    chara_bust_size = IntegerField()
    chara_face_model = IntegerField()
    chara_hair_color = IntegerField()
    chara_hair_model = IntegerField()
    chara_height = IntegerField()
    chara_skin_color = IntegerField()
    default_personality = IntegerField()
    dress_color_id = IntegerField()
    dress_id = IntegerField()
    hair_cutoff = IntegerField()
    mob_id = AutoField()
    race_personality = IntegerField()
    race_running_type = IntegerField()
    sex = IntegerField()
    socks = IntegerField()
    use_live = IntegerField()

    class Meta:
        table_name = 'mob_data'

class MobDressColorSet(BaseModel):
    color_b1 = TextField()
    color_b2 = TextField()
    color_g1 = TextField()
    color_g2 = TextField()
    color_r1 = TextField()
    color_r2 = TextField()
    toon_color_b1 = TextField()
    toon_color_b2 = TextField()
    toon_color_g1 = TextField()
    toon_color_g2 = TextField()
    toon_color_r1 = TextField()
    toon_color_r2 = TextField()

    class Meta:
        table_name = 'mob_dress_color_set'

class MobHairColorSet(BaseModel):
    eye_color_b1 = TextField()
    eye_color_b2 = TextField()
    eye_color_g1 = TextField()
    eye_color_g2 = TextField()
    eye_color_r1 = TextField()
    eye_color_r2 = TextField()
    hair_color_b1 = TextField()
    hair_color_b2 = TextField()
    hair_color_g1 = TextField()
    hair_color_g2 = TextField()
    hair_color_r1 = TextField()
    hair_color_r2 = TextField()
    hair_toon_color_b1 = TextField()
    hair_toon_color_b2 = TextField()
    hair_toon_color_g1 = TextField()
    hair_toon_color_g2 = TextField()
    hair_toon_color_r1 = TextField()
    hair_toon_color_r2 = TextField()
    mayu_color_b1 = TextField()
    mayu_color_b2 = TextField()
    mayu_color_g1 = TextField()
    mayu_color_g2 = TextField()
    mayu_color_r1 = TextField()
    mayu_color_r2 = TextField()
    mayu_toon_color_b1 = TextField()
    mayu_toon_color_b2 = TextField()
    mayu_toon_color_g1 = TextField()
    mayu_toon_color_g2 = TextField()
    mayu_toon_color_r1 = TextField()
    mayu_toon_color_r2 = TextField()
    tail_color_b1 = TextField()
    tail_color_b2 = TextField()
    tail_color_g1 = TextField()
    tail_color_g2 = TextField()
    tail_color_r1 = TextField()
    tail_color_r2 = TextField()
    tail_toon_color_b1 = TextField()
    tail_toon_color_b2 = TextField()
    tail_toon_color_g1 = TextField()
    tail_toon_color_g2 = TextField()
    tail_toon_color_r1 = TextField()
    tail_toon_color_r2 = TextField()

    class Meta:
        table_name = 'mob_hair_color_set'

class NeedPieceNumData(BaseModel):
    piece_num = IntegerField()
    rarity = IntegerField(unique=True)

    class Meta:
        table_name = 'need_piece_num_data'

class Nickname(BaseModel):
    chara_data_id = IntegerField()
    disp_order = IntegerField()
    end_date = IntegerField()
    group_id = IntegerField()
    rank = IntegerField()
    receive_condition_type = IntegerField()
    start_date = IntegerField()
    user_show = IntegerField(index=True)

    class Meta:
        table_name = 'nickname'

class NoteProfile(BaseModel):
    chara_id = IntegerField(index=True)
    lock_type = IntegerField()
    lock_value = IntegerField()
    sort = IntegerField()
    text_type = IntegerField()

    class Meta:
        table_name = 'note_profile'

class NoteProfileTextType(BaseModel):
    sort = IntegerField()
    text_category_id = IntegerField()
    text_type = IntegerField(index=True)

    class Meta:
        table_name = 'note_profile_text_type'

class PieceData(BaseModel):
    end_date = TextField()
    item_place_id = IntegerField()
    start_date = TextField()

    class Meta:
        table_name = 'piece_data'

class PriceChange(BaseModel):
    group_id = IntegerField(index=True)
    max_num = IntegerField()
    min_num = IntegerField()
    pay_item_num = IntegerField()

    class Meta:
        table_name = 'price_change'

class Race(BaseModel):
    course_set = IntegerField(index=True)
    entry_num = IntegerField()
    ff_anim = IntegerField()
    ff_camera = IntegerField()
    ff_camera_sub = IntegerField()
    ff_cue_name = TextField()
    ff_cuesheet_name = TextField()
    ff_sub = IntegerField()
    goal_flower = IntegerField()
    goal_gate = IntegerField()
    grade = IntegerField()
    group = IntegerField(index=True)
    thumbnail_id = IntegerField()

    class Meta:
        table_name = 'race'

class RaceBgm(BaseModel):
    entrytable_bgm_cue_name = TextField()
    entrytable_bgm_cuesheet_name = TextField()
    first_bgm_pattern = IntegerField()
    grade = IntegerField()
    paddock_bgm_cue_name = TextField()
    paddock_bgm_cuesheet_name = TextField()
    race_instance_id = IntegerField()
    race_type = IntegerField(index=True)
    result_cutin_bgm_cue_name_1 = TextField()
    result_cutin_bgm_cue_name_2 = TextField()
    result_cutin_bgm_cue_name_3 = TextField()
    result_cutin_bgm_cuesheet_name_1 = TextField()
    result_cutin_bgm_cuesheet_name_2 = TextField()
    result_cutin_bgm_cuesheet_name_3 = TextField()
    result_list_bgm_cue_name_1 = TextField()
    result_list_bgm_cue_name_2 = TextField()
    result_list_bgm_cue_name_3 = TextField()
    result_list_bgm_cuesheet_name_1 = TextField()
    result_list_bgm_cuesheet_name_2 = TextField()
    result_list_bgm_cuesheet_name_3 = TextField()
    second_bgm_pattern = IntegerField()
    single_mode_program_id = IntegerField()
    single_mode_route_race_id = IntegerField()

    class Meta:
        table_name = 'race_bgm'

class RaceBgmCutinExtensionTime(BaseModel):
    card_id = IntegerField()
    chara_id = IntegerField()
    cutin_category = IntegerField(index=True)
    extension_sec = IntegerField()
    extension_sec_long = IntegerField()

    class Meta:
        table_name = 'race_bgm_cutin_extension_time'

class RaceBgmPattern(BaseModel):
    bgm_cue_name_1 = TextField()
    bgm_cue_name_10 = TextField()
    bgm_cue_name_11 = TextField()
    bgm_cue_name_12 = TextField()
    bgm_cue_name_13 = TextField()
    bgm_cue_name_14 = TextField()
    bgm_cue_name_15 = TextField()
    bgm_cue_name_16 = TextField()
    bgm_cue_name_17 = TextField()
    bgm_cue_name_18 = TextField()
    bgm_cue_name_19 = TextField()
    bgm_cue_name_2 = TextField()
    bgm_cue_name_20 = TextField()
    bgm_cue_name_21 = TextField()
    bgm_cue_name_22 = TextField()
    bgm_cue_name_23 = TextField()
    bgm_cue_name_24 = TextField()
    bgm_cue_name_25 = TextField()
    bgm_cue_name_26 = TextField()
    bgm_cue_name_27 = TextField()
    bgm_cue_name_28 = TextField()
    bgm_cue_name_29 = TextField()
    bgm_cue_name_3 = TextField()
    bgm_cue_name_30 = TextField()
    bgm_cue_name_4 = TextField()
    bgm_cue_name_5 = TextField()
    bgm_cue_name_6 = TextField()
    bgm_cue_name_7 = TextField()
    bgm_cue_name_8 = TextField()
    bgm_cue_name_9 = TextField()
    bgm_cuesheet_name_1 = TextField()
    bgm_cuesheet_name_10 = TextField()
    bgm_cuesheet_name_11 = TextField()
    bgm_cuesheet_name_12 = TextField()
    bgm_cuesheet_name_13 = TextField()
    bgm_cuesheet_name_14 = TextField()
    bgm_cuesheet_name_15 = TextField()
    bgm_cuesheet_name_16 = TextField()
    bgm_cuesheet_name_17 = TextField()
    bgm_cuesheet_name_18 = TextField()
    bgm_cuesheet_name_19 = TextField()
    bgm_cuesheet_name_2 = TextField()
    bgm_cuesheet_name_20 = TextField()
    bgm_cuesheet_name_21 = TextField()
    bgm_cuesheet_name_22 = TextField()
    bgm_cuesheet_name_23 = TextField()
    bgm_cuesheet_name_24 = TextField()
    bgm_cuesheet_name_25 = TextField()
    bgm_cuesheet_name_26 = TextField()
    bgm_cuesheet_name_27 = TextField()
    bgm_cuesheet_name_28 = TextField()
    bgm_cuesheet_name_29 = TextField()
    bgm_cuesheet_name_3 = TextField()
    bgm_cuesheet_name_30 = TextField()
    bgm_cuesheet_name_4 = TextField()
    bgm_cuesheet_name_5 = TextField()
    bgm_cuesheet_name_6 = TextField()
    bgm_cuesheet_name_7 = TextField()
    bgm_cuesheet_name_8 = TextField()
    bgm_cuesheet_name_9 = TextField()
    bgm_time_1 = IntegerField()
    bgm_time_10 = IntegerField()
    bgm_time_11 = IntegerField()
    bgm_time_12 = IntegerField()
    bgm_time_13 = IntegerField()
    bgm_time_14 = IntegerField()
    bgm_time_15 = IntegerField()
    bgm_time_16 = IntegerField()
    bgm_time_17 = IntegerField()
    bgm_time_18 = IntegerField()
    bgm_time_19 = IntegerField()
    bgm_time_2 = IntegerField()
    bgm_time_20 = IntegerField()
    bgm_time_21 = IntegerField()
    bgm_time_22 = IntegerField()
    bgm_time_23 = IntegerField()
    bgm_time_24 = IntegerField()
    bgm_time_25 = IntegerField()
    bgm_time_26 = IntegerField()
    bgm_time_27 = IntegerField()
    bgm_time_28 = IntegerField()
    bgm_time_29 = IntegerField()
    bgm_time_3 = IntegerField()
    bgm_time_30 = IntegerField()
    bgm_time_4 = IntegerField()
    bgm_time_5 = IntegerField()
    bgm_time_6 = IntegerField()
    bgm_time_7 = IntegerField()
    bgm_time_8 = IntegerField()
    bgm_time_9 = IntegerField()

    class Meta:
        table_name = 'race_bgm_pattern'

class RaceBibColor(BaseModel):
    bib_color = IntegerField()
    font_color = IntegerField()
    grade = IntegerField()
    race_id = IntegerField()

    class Meta:
        table_name = 'race_bib_color'
        indexes = (
            (('grade', 'race_id'), True),
        )
        primary_key = CompositeKey('grade', 'race_id')

class RaceCondition(BaseModel):
    ground = IntegerField()
    rate = IntegerField()
    season = IntegerField()
    weather = IntegerField()

    class Meta:
        table_name = 'race_condition'
        indexes = (
            (('ground', 'weather'), False),
            (('season', 'ground'), False),
            (('season', 'weather'), False),
            (('weather', 'ground'), False),
        )

class RaceCourseSet(BaseModel):
    course_set_status_id = IntegerField()
    distance = IntegerField()
    fence_set = IntegerField()
    finish_time_max = IntegerField()
    finish_time_max_random_range = IntegerField()
    finish_time_min = IntegerField()
    finish_time_min_random_range = IntegerField()
    float_lane_max = IntegerField()
    ground = IntegerField()
    inout = IntegerField()
    race_track_id = IntegerField(index=True)
    turn = IntegerField()

    class Meta:
        table_name = 'race_course_set'

class RaceCourseSetStatus(BaseModel):
    course_set_status_id = AutoField()
    target_status_1 = IntegerField()
    target_status_2 = IntegerField()

    class Meta:
        table_name = 'race_course_set_status'

class RaceEnvDefine(BaseModel):
    race_track_id = IntegerField(index=True)
    resource = IntegerField()
    season = IntegerField()
    timezone = IntegerField()
    weather = IntegerField()

    class Meta:
        table_name = 'race_env_define'

class RaceFenceSet(BaseModel):
    fence_1 = IntegerField()
    fence_2 = IntegerField()
    fence_3 = IntegerField()
    fence_4 = IntegerField()
    fence_5 = IntegerField()
    fence_6 = IntegerField()
    fence_7 = IntegerField()
    fence_8 = IntegerField()

    class Meta:
        table_name = 'race_fence_set'

class RaceInstance(BaseModel):
    date = IntegerField()
    npc_group_id = IntegerField()
    race_id = IntegerField(index=True)
    race_number = IntegerField()
    time = IntegerField()

    class Meta:
        table_name = 'race_instance'

class RaceJikkyoBase(BaseModel):
    camera_horse1 = IntegerField()
    camera_horse2 = IntegerField()
    camera_id = IntegerField()
    comment_group = IntegerField()
    disable_reentry_situation = IntegerField()
    disable_reuse = IntegerField()
    discard = IntegerField()
    immediate = IntegerField()
    message_group = IntegerField()
    mode = IntegerField(index=True)
    per = IntegerField()
    priority = IntegerField()
    situation = IntegerField()
    situation_end = IntegerField()
    sub_mode = IntegerField()
    sub_mode_jump = IntegerField()
    sub_situation = IntegerField()
    tension = IntegerField()
    trigger0 = IntegerField()
    trigger1 = IntegerField()
    trigger2 = IntegerField()
    trigger3 = IntegerField()
    trigger4 = IntegerField()
    trigger5 = IntegerField()
    trigger6 = IntegerField()
    trigger7 = IntegerField()
    trigger8 = IntegerField()
    trigger9 = IntegerField()

    class Meta:
        table_name = 'race_jikkyo_base'

class RaceJikkyoComment(BaseModel):
    group_id = IntegerField(index=True)
    message = TextField()
    message_group = IntegerField()
    per = IntegerField()
    voice = TextField()

    class Meta:
        table_name = 'race_jikkyo_comment'

class RaceJikkyoCue(BaseModel):
    cuesheet_id = IntegerField()
    cuesheet_type = IntegerField(index=True)
    id = IntegerField()

    class Meta:
        table_name = 'race_jikkyo_cue'
        indexes = (
            (('id', 'cuesheet_type'), True),
        )
        primary_key = CompositeKey('cuesheet_type', 'id')

class RaceJikkyoMessage(BaseModel):
    comment_group = IntegerField(index=True)
    group_id = IntegerField(index=True)
    message = TextField()
    per = IntegerField()
    reuse = IntegerField()
    voice = TextField()

    class Meta:
        table_name = 'race_jikkyo_message'

class RaceJikkyoRace(BaseModel):
    cue_id = IntegerField()

    class Meta:
        table_name = 'race_jikkyo_race'

class RaceJikkyoTrigger(BaseModel):
    command = IntegerField()
    horse1 = IntegerField()
    horse2 = IntegerField()
    inequality = IntegerField()
    param1 = IntegerField()
    param2 = IntegerField()

    class Meta:
        table_name = 'race_jikkyo_trigger'

class RaceMotivationRate(BaseModel):
    motivation_rate = IntegerField()

    class Meta:
        table_name = 'race_motivation_rate'

class RaceOverrunPattern(BaseModel):
    finish_order_0_type = IntegerField()
    finish_order_1_type = IntegerField()
    finish_order_2_type = IntegerField()
    finish_order_3_type = IntegerField()
    finish_order_4_type = IntegerField()
    finish_order_lose_type = IntegerField()

    class Meta:
        table_name = 'race_overrun_pattern'

class RacePlayerCamera(BaseModel):
    category = IntegerField(index=True)
    prefab_name = TextField(index=True)
    priority = IntegerField()

    class Meta:
        table_name = 'race_player_camera'

class RacePopularityProperValue(BaseModel):
    proper_grade = IntegerField()
    proper_type = IntegerField(index=True)
    value = IntegerField()

    class Meta:
        table_name = 'race_popularity_proper_value'

class RaceProperDistanceRate(BaseModel):
    proper_rate_power = IntegerField()
    proper_rate_speed = IntegerField()

    class Meta:
        table_name = 'race_proper_distance_rate'

class RaceProperGroundRate(BaseModel):
    proper_rate = IntegerField()

    class Meta:
        table_name = 'race_proper_ground_rate'

class RaceProperRunningstyleRate(BaseModel):
    proper_rate = IntegerField()

    class Meta:
        table_name = 'race_proper_runningstyle_rate'

class RaceTrack(BaseModel):
    enable_half_gate = IntegerField()
    footsmoke_color_type = IntegerField()
    horse_num_gate_variation = IntegerField()
    initial_lane_type = IntegerField()
    turf_vision_type = IntegerField()

    class Meta:
        table_name = 'race_track'

class RaceTrophy(BaseModel):
    disp_order = IntegerField()
    display_end_date = TextField()
    event_type = IntegerField()
    original_flag = IntegerField()
    race_instance_id = IntegerField(unique=True)
    size = IntegerField()
    start_date = TextField()
    trophy_id = IntegerField(index=True)

    class Meta:
        table_name = 'race_trophy'

class RaceTrophyReward(BaseModel):
    item_category = IntegerField()
    item_id = IntegerField()
    item_num = IntegerField()
    trophy_id = AutoField()

    class Meta:
        table_name = 'race_trophy_reward'

class RandomEarTailMotion(BaseModel):
    ear_type = IntegerField()
    motion_name = TextField()
    parts_type = IntegerField(index=True)
    use_story = IntegerField()

    class Meta:
        table_name = 'random_ear_tail_motion'

class SeasonData(BaseModel):
    end_date = TextField()
    priority = IntegerField()
    season = IntegerField()
    start_date = TextField()
    type = IntegerField(index=True)

    class Meta:
        table_name = 'season_data'

class ShortEpisode(BaseModel):
    condition_type = IntegerField()
    condition_value_1 = IntegerField()
    scene = IntegerField(index=True)
    sort = IntegerField()
    story_id = IntegerField()

    class Meta:
        table_name = 'short_episode'

class SingleModeAnalyzeMessage(BaseModel):
    character_type = IntegerField()
    motion_type = IntegerField()
    popularity = IntegerField(index=True)
    priority = IntegerField()
    proper_distance = IntegerField()
    proper_ground = IntegerField()
    rate = IntegerField()
    year = IntegerField()

    class Meta:
        table_name = 'single_mode_analyze_message'

class SingleModeAnalyzeTicket(BaseModel):
    cost_ticket = IntegerField()
    grade = IntegerField(index=True)

    class Meta:
        table_name = 'single_mode_analyze_ticket'

class SingleModeCharaEffect(BaseModel):
    effect_category = IntegerField()
    effect_group_id = IntegerField()
    effect_type = IntegerField()
    priority = IntegerField()

    class Meta:
        table_name = 'single_mode_chara_effect'

class SingleModeCharaGrade(BaseModel):
    need_fan_count = IntegerField()
    run_num = IntegerField()
    win_num = IntegerField()

    class Meta:
        table_name = 'single_mode_chara_grade'

class SingleModeCharaProgram(BaseModel):
    chara_id = IntegerField(index=True)
    program_group = IntegerField()

    class Meta:
        table_name = 'single_mode_chara_program'

class SingleModeConclusionSet(BaseModel):
    conclusion_id = IntegerField()
    root_id = IntegerField()
    story_id = IntegerField(index=True)

    class Meta:
        table_name = 'single_mode_conclusion_set'
        primary_key = False

class SingleModeEvaluation(BaseModel):
    chara_id = IntegerField(index=True)
    evaluation = IntegerField()

    class Meta:
        table_name = 'single_mode_evaluation'

class SingleModeEventConclusion(BaseModel):
    chara_id = IntegerField()
    chara_motion_set_id = IntegerField()
    id = IntegerField()

    class Meta:
        table_name = 'single_mode_event_conclusion'
        indexes = (
            (('id', 'chara_id'), True),
        )
        primary_key = CompositeKey('chara_id', 'id')

class SingleModeEventProduction(BaseModel):
    event_category_id = IntegerField()
    max_item_id = IntegerField()
    story_id = AutoField()

    class Meta:
        table_name = 'single_mode_event_production'

class SingleModeFanCount(BaseModel):
    fan_count = IntegerField()
    fan_set_id = IntegerField(index=True)
    order = IntegerField()

    class Meta:
        table_name = 'single_mode_fan_count'

class SingleModeHintGain(BaseModel):
    hint_gain_type = IntegerField()
    hint_group = IntegerField()
    hint_id = IntegerField(index=True)
    hint_value_1 = IntegerField()
    hint_value_2 = IntegerField()
    id = IntegerField()
    support_card_id = IntegerField()

    class Meta:
        table_name = 'single_mode_hint_gain'
        primary_key = False

class SingleModeMessage(BaseModel):
    character_type = IntegerField()
    emergent = IntegerField()
    priority = IntegerField()
    status_type_1 = IntegerField()
    status_type_2 = IntegerField()
    status_value_1_1 = IntegerField()
    status_value_1_2 = IntegerField()
    status_value_2_1 = IntegerField()
    status_value_2_2 = IntegerField()

    class Meta:
        table_name = 'single_mode_message'

class SingleModeNpc(BaseModel):
    chara_id = IntegerField()
    guts = IntegerField()
    mob_id = IntegerField()
    motivation_max = IntegerField()
    motivation_min = IntegerField()
    npc_group_id = IntegerField(index=True)
    pow = IntegerField()
    proper_distance_long = IntegerField()
    proper_distance_middle = IntegerField()
    proper_distance_mile = IntegerField()
    proper_distance_short = IntegerField()
    proper_ground_dirt = IntegerField()
    proper_ground_turf = IntegerField()
    proper_running_style_nige = IntegerField()
    proper_running_style_oikomi = IntegerField()
    proper_running_style_sashi = IntegerField()
    proper_running_style_senko = IntegerField()
    race_dress_id = IntegerField()
    skill_set_id = IntegerField()
    speed = IntegerField()
    stamina = IntegerField()
    wiz = IntegerField()

    class Meta:
        table_name = 'single_mode_npc'

class SingleModeOuting(BaseModel):
    command_group_id = IntegerField(index=True)
    condition = IntegerField()
    is_play_cutt = IntegerField()

    class Meta:
        table_name = 'single_mode_outing'

class SingleModeOutingSet(BaseModel):
    command_group_id_1 = IntegerField()
    command_group_id_2 = IntegerField()
    command_group_id_3 = IntegerField()
    command_group_id_4 = IntegerField()
    command_group_id_5 = IntegerField()

    class Meta:
        table_name = 'single_mode_outing_set'

class SingleModeProgram(BaseModel):
    base_program_id = IntegerField()
    entry_decrease = IntegerField()
    entry_decrease_flag = IntegerField()
    fan_set_id = IntegerField()
    filly_only_flag = IntegerField()
    grade_rate_id = IntegerField()
    half = IntegerField()
    month = IntegerField(index=True)
    need_fan_count = IntegerField()
    program_group = IntegerField()
    race_instance_id = IntegerField()
    race_permission = IntegerField()
    recommend_class_id = IntegerField()
    reward_set_id = IntegerField()

    class Meta:
        table_name = 'single_mode_program'

class SingleModeRaceGroup(BaseModel):
    race_group_id = IntegerField(index=True)
    race_program_id = IntegerField()

    class Meta:
        table_name = 'single_mode_race_group'

class SingleModeRaceLive(BaseModel):
    grade = IntegerField()
    music_id = IntegerField()
    race_instance_id = IntegerField()

    class Meta:
        table_name = 'single_mode_race_live'

class SingleModeRank(BaseModel):
    max_value = IntegerField()
    min_value = IntegerField()

    class Meta:
        table_name = 'single_mode_rank'

class SingleModeRecommend(BaseModel):
    grade_lower_limit = IntegerField()
    grade_upper_limit = IntegerField()

    class Meta:
        table_name = 'single_mode_recommend'

class SingleModeRecommendSetting(BaseModel):
    header_font_color = TextField()
    recommend_course_id = IntegerField(index=True)

    class Meta:
        table_name = 'single_mode_recommend_setting'

class SingleModeRewardSet(BaseModel):
    bonus = IntegerField()
    item_category = IntegerField()
    item_id = IntegerField()
    item_num = IntegerField()
    odds = IntegerField()
    order_max = IntegerField()
    order_min = IntegerField()
    reward_set_id = IntegerField(index=True)
    reward_type = IntegerField()

    class Meta:
        table_name = 'single_mode_reward_set'

class SingleModeRival(BaseModel):
    chara_id = IntegerField()
    condition_type = IntegerField()
    race_program_id = IntegerField(index=True)
    rival_chara_id = IntegerField()
    single_mode_npc_id = IntegerField()
    turn = IntegerField()

    class Meta:
        table_name = 'single_mode_rival'
        indexes = (
            (('chara_id', 'turn', 'race_program_id', 'rival_chara_id'), True),
        )

class SingleModeRoute(BaseModel):
    chara_id = IntegerField()
    race_set_id = IntegerField()
    scenario_id = IntegerField()

    class Meta:
        table_name = 'single_mode_route'

class SingleModeRouteRace(BaseModel):
    condition_id = IntegerField()
    condition_type = IntegerField()
    condition_value_1 = IntegerField()
    condition_value_2 = IntegerField()
    determine_race = IntegerField()
    determine_race_flag = IntegerField()
    race_set_id = IntegerField(index=True)
    race_type = IntegerField()
    sort_id = IntegerField()
    target_type = IntegerField()
    turn = IntegerField()

    class Meta:
        table_name = 'single_mode_route_race'

class SingleModeScenario(BaseModel):
    end_date = IntegerField()
    prologue_id = IntegerField()
    scenario_image_id = IntegerField()
    sort_id = IntegerField()
    start_date = IntegerField()
    turn_set_id = IntegerField()

    class Meta:
        table_name = 'single_mode_scenario'

class SingleModeSkillNeedPoint(BaseModel):
    need_skill_point = IntegerField()
    status_type = IntegerField()
    status_value = IntegerField()

    class Meta:
        table_name = 'single_mode_skill_need_point'

class SingleModeStoryData(BaseModel):
    card_chara_id = IntegerField(index=True)
    card_id = IntegerField(index=True)
    ending_type = IntegerField()
    event_title_chara_icon = IntegerField()
    event_title_dress_icon = IntegerField()
    event_title_style = IntegerField()
    mini_game_result = IntegerField()
    race_event_flag = IntegerField()
    se_change = IntegerField()
    short_story_id = IntegerField(index=True)
    show_clear = IntegerField()
    show_progress_1 = IntegerField()
    show_progress_2 = IntegerField()
    show_succession = IntegerField()
    story_id = IntegerField(index=True)
    support_card_id = IntegerField(index=True)
    support_chara_id = IntegerField(index=True)

    class Meta:
        table_name = 'single_mode_story_data'

class SingleModeTagCardPos(BaseModel):
    pattern = IntegerField()
    pos_index = IntegerField()
    pos_x = IntegerField()
    pos_y = IntegerField()
    rot_z = IntegerField()
    scale_x = IntegerField()
    scale_y = IntegerField()
    support_card_id = IntegerField(index=True)

    class Meta:
        table_name = 'single_mode_tag_card_pos'

class SingleModeTopBg(BaseModel):
    bg_id = IntegerField()
    bg_sub_id = IntegerField()
    month = IntegerField(index=True)

    class Meta:
        table_name = 'single_mode_top_bg'

class SingleModeTraining(BaseModel):
    base_command_id = IntegerField()
    command_id = IntegerField(index=True)
    command_level = IntegerField()
    command_type = IntegerField(index=True)
    cutin_file_id = IntegerField(index=True)
    dress_id = IntegerField()
    dress_type = IntegerField()
    env_cue_name = TextField()
    env_cuesheet_name = TextField()
    failure_rate = IntegerField()
    max_chara_num = IntegerField()
    menu_bg_id = IntegerField()
    menu_bg_sub_id = IntegerField()
    motion_set = IntegerField()
    sabori_type = IntegerField()

    class Meta:
        table_name = 'single_mode_training'
        indexes = (
            (('command_id', 'command_level'), True),
        )

class SingleModeTrainingEffect(BaseModel):
    command_id = IntegerField()
    effect_value = IntegerField()
    result_state = IntegerField()
    scenario_id = IntegerField()
    sub_id = IntegerField()
    target_type = IntegerField()

    class Meta:
        table_name = 'single_mode_training_effect'
        indexes = (
            (('command_id', 'result_state'), False),
        )

class SingleModeTrainingSe(BaseModel):
    chara_index = IntegerField()
    se_cue_name = TextField()
    se_cuesheet_name = TextField()
    sheet_id = TextField(index=True)
    skip_se_cue_name = TextField()
    skip_se_cuesheet_name = TextField()
    voice_trigger_id = IntegerField()

    class Meta:
        table_name = 'single_mode_training_se'

class SingleModeTurn(BaseModel):
    bgm_cue_name = TextField()
    bgm_cuesheet_name = TextField()
    env_cue_name = TextField()
    env_cuesheet_name = TextField()
    half = IntegerField()
    health_room_type = IntegerField()
    month = IntegerField()
    outing_set_id = IntegerField()
    period = IntegerField()
    race_entry_type = IntegerField()
    rest_type = IntegerField()
    story_bg_id = IntegerField()
    story_bg_sub_id = IntegerField()
    story_cloth_id = IntegerField()
    top_bg_id = IntegerField()
    top_cloth_id = IntegerField()
    training_set_id = IntegerField()
    turn = IntegerField()
    turn_set_id = IntegerField(index=True)
    unique_command = IntegerField()
    year = IntegerField()

    class Meta:
        table_name = 'single_mode_turn'

class SingleModeUniqueChara(BaseModel):
    chara_id = IntegerField()
    partner_id = IntegerField()
    period = IntegerField()
    scenario_id = IntegerField()
    training_placement = IntegerField()

    class Meta:
        table_name = 'single_mode_unique_chara'
        indexes = (
            (('partner_id', 'scenario_id'), False),
        )

class SingleModeWinsSaddle(BaseModel):
    condition = IntegerField()
    group_id = IntegerField()
    priority = IntegerField()
    race_instance_id_1 = IntegerField()
    race_instance_id_2 = IntegerField()
    race_instance_id_3 = IntegerField()
    race_instance_id_4 = IntegerField()
    race_instance_id_5 = IntegerField()
    race_instance_id_6 = IntegerField()
    race_instance_id_7 = IntegerField()
    race_instance_id_8 = IntegerField()
    win_saddle_type = IntegerField()

    class Meta:
        table_name = 'single_mode_wins_saddle'

class SkillData(BaseModel):
    ability_type_1_1 = IntegerField()
    ability_type_1_2 = IntegerField()
    ability_type_1_3 = IntegerField()
    ability_type_2_1 = IntegerField()
    ability_type_2_2 = IntegerField()
    ability_type_2_3 = IntegerField()
    ability_value_level_usage_1_1 = IntegerField()
    ability_value_level_usage_1_2 = IntegerField()
    ability_value_level_usage_1_3 = IntegerField()
    ability_value_level_usage_2_1 = IntegerField()
    ability_value_level_usage_2_2 = IntegerField()
    ability_value_level_usage_2_3 = IntegerField()
    ability_value_usage_1_1 = IntegerField()
    ability_value_usage_1_2 = IntegerField()
    ability_value_usage_1_3 = IntegerField()
    ability_value_usage_2_1 = IntegerField()
    ability_value_usage_2_2 = IntegerField()
    ability_value_usage_2_3 = IntegerField()
    activate_lot = IntegerField()
    condition_1 = TextField()
    condition_2 = TextField()
    disp_order = IntegerField()
    exp_type = IntegerField()
    filter_switch = IntegerField()
    float_ability_time_1 = IntegerField()
    float_ability_time_2 = IntegerField()
    float_ability_value_1_1 = IntegerField()
    float_ability_value_1_2 = IntegerField()
    float_ability_value_1_3 = IntegerField()
    float_ability_value_2_1 = IntegerField()
    float_ability_value_2_2 = IntegerField()
    float_ability_value_2_3 = IntegerField()
    float_cooldown_time_1 = IntegerField()
    float_cooldown_time_2 = IntegerField()
    grade_value = IntegerField()
    group_id = IntegerField(index=True)
    group_rate = IntegerField()
    icon_id = IntegerField()
    popularity_add_param_1 = IntegerField()
    popularity_add_param_2 = IntegerField()
    popularity_add_value_1 = IntegerField()
    popularity_add_value_2 = IntegerField()
    potential_per_default = IntegerField()
    rarity = IntegerField()
    skill_category = IntegerField()
    tag_id = TextField()
    target_type_1_1 = IntegerField()
    target_type_1_2 = IntegerField()
    target_type_1_3 = IntegerField()
    target_type_2_1 = IntegerField()
    target_type_2_2 = IntegerField()
    target_type_2_3 = IntegerField()
    target_value_1_1 = IntegerField()
    target_value_1_2 = IntegerField()
    target_value_1_3 = IntegerField()
    target_value_2_1 = IntegerField()
    target_value_2_2 = IntegerField()
    target_value_2_3 = IntegerField()
    unique_skill_id_1 = IntegerField()
    unique_skill_id_2 = IntegerField()

    class Meta:
        table_name = 'skill_data'

class SkillExp(BaseModel):
    level = IntegerField()
    scale = IntegerField()
    type = IntegerField(index=True)

    class Meta:
        table_name = 'skill_exp'

class SkillLevelValue(BaseModel):
    ability_type = IntegerField(index=True)
    float_ability_value_coef = IntegerField()
    level = IntegerField()

    class Meta:
        table_name = 'skill_level_value'

class SkillRarity(BaseModel):
    value = IntegerField()

    class Meta:
        table_name = 'skill_rarity'

class SkillSet(BaseModel):
    skill_id1 = IntegerField()
    skill_id10 = IntegerField()
    skill_id2 = IntegerField()
    skill_id3 = IntegerField()
    skill_id4 = IntegerField()
    skill_id5 = IntegerField()
    skill_id6 = IntegerField()
    skill_id7 = IntegerField()
    skill_id8 = IntegerField()
    skill_id9 = IntegerField()
    skill_level1 = IntegerField()
    skill_level10 = IntegerField()
    skill_level2 = IntegerField()
    skill_level3 = IntegerField()
    skill_level4 = IntegerField()
    skill_level5 = IntegerField()
    skill_level6 = IntegerField()
    skill_level7 = IntegerField()
    skill_level8 = IntegerField()
    skill_level9 = IntegerField()

    class Meta:
        table_name = 'skill_set'

class SqliteStat1(BaseModel):
    idx = BareField(null=True)
    stat = BareField(null=True)
    tbl = BareField(null=True)

    class Meta:
        table_name = 'sqlite_stat1'
        primary_key = False

class StoryEventBingoReward(BaseModel):
    item_category = IntegerField()
    item_id = IntegerField()
    item_num = IntegerField()
    line_num = IntegerField()
    reward_set_id = IntegerField(index=True)

    class Meta:
        table_name = 'story_event_bingo_reward'

class StoryEventBonusCard(BaseModel):
    card_id = IntegerField()
    chara_id = IntegerField()
    end_date = IntegerField()
    rarity_1 = IntegerField()
    rarity_2 = IntegerField()
    rarity_3 = IntegerField()
    rarity_4 = IntegerField()
    rarity_5 = IntegerField()
    start_date = IntegerField()
    story_event_id = IntegerField(index=True)

    class Meta:
        table_name = 'story_event_bonus_card'
        indexes = (
            (('story_event_id', 'chara_id', 'card_id'), True),
        )

class StoryEventBonusSupportCard(BaseModel):
    chara_id = IntegerField()
    end_date = IntegerField()
    limit_0 = IntegerField()
    limit_1 = IntegerField()
    limit_2 = IntegerField()
    limit_3 = IntegerField()
    limit_4 = IntegerField()
    rarity = IntegerField()
    start_date = IntegerField()
    story_event_id = IntegerField(index=True)
    support_card_id = IntegerField()

    class Meta:
        table_name = 'story_event_bonus_support_card'
        indexes = (
            (('story_event_id', 'chara_id', 'rarity', 'support_card_id'), True),
        )

class StoryEventData(BaseModel):
    end_date = IntegerField()
    ending_date = IntegerField()
    middle_date_01 = IntegerField()
    middle_date_02 = IntegerField()
    notice_date = IntegerField()
    start_date = IntegerField()
    story_event_id = AutoField()

    class Meta:
        table_name = 'story_event_data'

class StoryEventMission(BaseModel):
    condition_num = IntegerField()
    condition_type = IntegerField()
    condition_value_1 = IntegerField()
    condition_value_2 = IntegerField()
    condition_value_3 = IntegerField()
    condition_value_4 = IntegerField()
    disp_order = IntegerField()
    item_category = IntegerField()
    item_id = IntegerField()
    item_num = IntegerField()
    mission_type = IntegerField()
    step_group_id = IntegerField()
    step_order = IntegerField()
    story_event_id = IntegerField(index=True)
    transition_type = IntegerField()

    class Meta:
        table_name = 'story_event_mission'

class StoryEventMissionTopChara(BaseModel):
    bgm_cue_name = TextField()
    bgm_cuesheet_name = TextField()
    character_id = IntegerField()
    dress_id = IntegerField()
    ending_flag = IntegerField()
    env_cue_name = TextField()
    env_cuesheet_name = TextField()
    menu_bg_id = IntegerField()
    menu_bg_sub_id = IntegerField()
    story_event_id = IntegerField(index=True)

    class Meta:
        table_name = 'story_event_mission_top_chara'

class StoryEventNicknameBonus(BaseModel):
    bonus_point = IntegerField()
    nickname_rank = IntegerField()
    story_event_id = IntegerField(index=True)

    class Meta:
        table_name = 'story_event_nickname_bonus'
        indexes = (
            (('story_event_id', 'nickname_rank'), True),
        )

class StoryEventPointReward(BaseModel):
    item_category = IntegerField()
    item_id = IntegerField()
    item_num = IntegerField()
    point = IntegerField()
    story_event_id = IntegerField(index=True)

    class Meta:
        table_name = 'story_event_point_reward'

class StoryEventRouletteBingo(BaseModel):
    can_loop = IntegerField()
    character_id = IntegerField()
    dress_id = IntegerField()
    end_date = IntegerField()
    reset_line = IntegerField()
    reward_set_id = IntegerField()
    roulette_id = IntegerField()
    sheet_num = IntegerField()
    start_date = IntegerField()
    story_event_id = IntegerField(index=True)
    use_item_category = IntegerField()
    use_item_id = IntegerField()
    use_item_num = IntegerField()

    class Meta:
        table_name = 'story_event_roulette_bingo'
        indexes = (
            (('roulette_id', 'story_event_id', 'sheet_num'), True),
        )

class StoryEventStoryData(BaseModel):
    add_reward_category_1 = IntegerField()
    add_reward_id_1 = IntegerField()
    add_reward_num_1 = IntegerField()
    episode_index_id = IntegerField()
    need_point = IntegerField()
    start_date = IntegerField()
    story_condition_type = IntegerField()
    story_event_id = IntegerField(index=True)
    story_id_1 = IntegerField()
    story_id_2 = IntegerField()
    story_id_3 = IntegerField()
    story_id_4 = IntegerField()
    story_id_5 = IntegerField()
    story_type_1 = IntegerField()
    story_type_2 = IntegerField()
    story_type_3 = IntegerField()
    story_type_4 = IntegerField()
    story_type_5 = IntegerField()

    class Meta:
        table_name = 'story_event_story_data'

class StoryEventTopChara(BaseModel):
    bgm_cue_name = TextField()
    bgm_cuesheet_name = TextField()
    character_id = IntegerField()
    dress_id = IntegerField()
    ending_flag = IntegerField()
    env_cue_name = TextField()
    env_cuesheet_name = TextField()
    max_episode_index = IntegerField()
    menu_bg_id = IntegerField()
    menu_bg_sub_id = IntegerField()
    min_episode_index = IntegerField()
    story_event_id = IntegerField(index=True)

    class Meta:
        table_name = 'story_event_top_chara'

class StoryEventWinBonus(BaseModel):
    bonus_point = IntegerField()
    max_win_count = IntegerField()
    min_win_count = IntegerField()
    story_event_id = IntegerField(index=True)

    class Meta:
        table_name = 'story_event_win_bonus'

class StoryLivePosition(BaseModel):
    chara_id = IntegerField()
    chara_type = IntegerField()
    dress_color = IntegerField()
    dress_id = IntegerField()
    music_id = IntegerField(index=True)
    position_id = IntegerField()
    second_dress_color = IntegerField()
    second_dress_id = IntegerField()
    vocal_chara_id = IntegerField()

    class Meta:
        table_name = 'story_live_position'

class StoryLiveSet(BaseModel):
    chara_id_1 = IntegerField()
    chara_id_10 = IntegerField()
    chara_id_11 = IntegerField()
    chara_id_12 = IntegerField()
    chara_id_13 = IntegerField()
    chara_id_14 = IntegerField()
    chara_id_15 = IntegerField()
    chara_id_16 = IntegerField()
    chara_id_17 = IntegerField()
    chara_id_18 = IntegerField()
    chara_id_2 = IntegerField()
    chara_id_3 = IntegerField()
    chara_id_4 = IntegerField()
    chara_id_5 = IntegerField()
    chara_id_6 = IntegerField()
    chara_id_7 = IntegerField()
    chara_id_8 = IntegerField()
    chara_id_9 = IntegerField()
    chara_type_1 = IntegerField()
    chara_type_10 = IntegerField()
    chara_type_11 = IntegerField()
    chara_type_12 = IntegerField()
    chara_type_13 = IntegerField()
    chara_type_14 = IntegerField()
    chara_type_15 = IntegerField()
    chara_type_16 = IntegerField()
    chara_type_17 = IntegerField()
    chara_type_18 = IntegerField()
    chara_type_2 = IntegerField()
    chara_type_3 = IntegerField()
    chara_type_4 = IntegerField()
    chara_type_5 = IntegerField()
    chara_type_6 = IntegerField()
    chara_type_7 = IntegerField()
    chara_type_8 = IntegerField()
    chara_type_9 = IntegerField()
    dress_color_1 = IntegerField()
    dress_color_10 = IntegerField()
    dress_color_11 = IntegerField()
    dress_color_12 = IntegerField()
    dress_color_13 = IntegerField()
    dress_color_14 = IntegerField()
    dress_color_15 = IntegerField()
    dress_color_16 = IntegerField()
    dress_color_17 = IntegerField()
    dress_color_18 = IntegerField()
    dress_color_2 = IntegerField()
    dress_color_3 = IntegerField()
    dress_color_4 = IntegerField()
    dress_color_5 = IntegerField()
    dress_color_6 = IntegerField()
    dress_color_7 = IntegerField()
    dress_color_8 = IntegerField()
    dress_color_9 = IntegerField()
    dress_id_1 = IntegerField()
    dress_id_10 = IntegerField()
    dress_id_11 = IntegerField()
    dress_id_12 = IntegerField()
    dress_id_13 = IntegerField()
    dress_id_14 = IntegerField()
    dress_id_15 = IntegerField()
    dress_id_16 = IntegerField()
    dress_id_17 = IntegerField()
    dress_id_18 = IntegerField()
    dress_id_2 = IntegerField()
    dress_id_3 = IntegerField()
    dress_id_4 = IntegerField()
    dress_id_5 = IntegerField()
    dress_id_6 = IntegerField()
    dress_id_7 = IntegerField()
    dress_id_8 = IntegerField()
    dress_id_9 = IntegerField()
    music_id = IntegerField(index=True)
    vocal_chara_id_1 = IntegerField()
    vocal_chara_id_2 = IntegerField()
    vocal_chara_id_3 = IntegerField()
    vocal_chara_id_4 = IntegerField()
    vocal_chara_id_5 = IntegerField()

    class Meta:
        table_name = 'story_live_set'

class StoryStill(BaseModel):
    order_id = IntegerField()
    page_id = IntegerField()
    still_id = IntegerField(index=True)

    class Meta:
        table_name = 'story_still'

class SuccessionFactor(BaseModel):
    effect_group_id = IntegerField()
    factor_group_id = IntegerField()
    factor_id = AutoField()
    factor_type = IntegerField()
    grade = IntegerField()
    rarity = IntegerField()

    class Meta:
        table_name = 'succession_factor'
        indexes = (
            (('factor_group_id', 'rarity'), True),
        )

class SuccessionFactorEffect(BaseModel):
    effect_id = IntegerField()
    factor_group_id = IntegerField(index=True)
    target_type = IntegerField()
    value_1 = IntegerField()
    value_2 = IntegerField()

    class Meta:
        table_name = 'succession_factor_effect'
        indexes = (
            (('factor_group_id', 'effect_id'), False),
        )

class SuccessionInitialFactor(BaseModel):
    add_point = IntegerField()
    factor_type = IntegerField(index=True)
    value_1 = IntegerField()
    value_2 = IntegerField()

    class Meta:
        table_name = 'succession_initial_factor'
        indexes = (
            (('factor_type', 'value_1'), False),
        )

class SuccessionRelation(BaseModel):
    relation_point = IntegerField()
    relation_type = AutoField()

    class Meta:
        table_name = 'succession_relation'

class SuccessionRelationMember(BaseModel):
    chara_id = IntegerField(index=True)
    relation_type = IntegerField()

    class Meta:
        table_name = 'succession_relation_member'

class SuccessionRelationRank(BaseModel):
    rank_value_max = IntegerField()
    rank_value_min = IntegerField()
    relation_rank = AutoField()

    class Meta:
        table_name = 'succession_relation_rank'

class SuccessionRental(BaseModel):
    rental_num = IntegerField()
    rental_rank = IntegerField()
    use_value1 = IntegerField()
    use_value2 = IntegerField()

    class Meta:
        table_name = 'succession_rental'
        indexes = (
            (('rental_rank', 'rental_num'), False),
        )

class SupportCardData(BaseModel):
    chara_id = IntegerField(index=True)
    command_id = IntegerField()
    command_type = IntegerField()
    detail_pos_x = IntegerField()
    detail_pos_y = IntegerField()
    detail_rot_z = IntegerField()
    detail_scale = IntegerField()
    effect_table_id = IntegerField()
    exchange_item_id = IntegerField()
    rarity = IntegerField()
    skill_set_id = IntegerField()
    support_card_type = IntegerField()
    unique_effect_id = IntegerField()

    class Meta:
        table_name = 'support_card_data'

class SupportCardEffectTable(BaseModel):
    id = IntegerField(index=True)
    init = IntegerField()
    limit_lv10 = IntegerField()
    limit_lv15 = IntegerField()
    limit_lv20 = IntegerField()
    limit_lv25 = IntegerField()
    limit_lv30 = IntegerField()
    limit_lv35 = IntegerField()
    limit_lv40 = IntegerField()
    limit_lv45 = IntegerField()
    limit_lv5 = IntegerField()
    limit_lv50 = IntegerField()
    type = IntegerField()

    class Meta:
        table_name = 'support_card_effect_table'
        indexes = (
            (('id', 'type'), True),
        )
        primary_key = CompositeKey('id', 'type')

class SupportCardLevel(BaseModel):
    level = IntegerField()
    rarity = IntegerField(index=True)
    total_exp = IntegerField()

    class Meta:
        table_name = 'support_card_level'
        indexes = (
            (('rarity', 'level'), True),
        )

class SupportCardLimit(BaseModel):
    limit_0 = IntegerField()
    limit_1 = IntegerField()
    limit_2 = IntegerField()
    limit_3 = IntegerField()
    limit_4 = IntegerField()
    rarity = AutoField()

    class Meta:
        table_name = 'support_card_limit'

class SupportCardTeamScoreBonus(BaseModel):
    level = IntegerField(index=True)
    score_rate = IntegerField()

    class Meta:
        table_name = 'support_card_team_score_bonus'

class SupportCardUniqueEffect(BaseModel):
    lv = IntegerField()
    type_0 = IntegerField()
    type_1 = IntegerField()
    value_0 = IntegerField()
    value_1 = IntegerField()

    class Meta:
        table_name = 'support_card_unique_effect'

class TeamStadium(BaseModel):
    calc_end_date = IntegerField()
    calc_end_time = TextField()
    calc_start_date = IntegerField()
    calc_start_time = TextField()
    end_date = TextField()
    interval_end_date = IntegerField()
    interval_end_time = TextField()
    interval_start_date = IntegerField()
    interval_start_time = TextField()
    race_end_date = IntegerField()
    race_end_time = TextField()
    race_start_date = IntegerField()
    race_start_time = TextField()
    start_date = TextField()

    class Meta:
        table_name = 'team_stadium'

class TeamStadiumBgm(BaseModel):
    cue_name = TextField()
    cuesheet_name = TextField()
    priority = IntegerField()
    scene_type = IntegerField(index=True)

    class Meta:
        table_name = 'team_stadium_bgm'

class TeamStadiumClass(BaseModel):
    class_down_range = IntegerField()
    class_up_range = IntegerField()
    team_class = IntegerField()
    team_stadium_id = IntegerField(index=True)
    unit_max_num = IntegerField()

    class Meta:
        table_name = 'team_stadium_class'

class TeamStadiumClassReward(BaseModel):
    class_reward_type = IntegerField()
    item_category_1 = IntegerField()
    item_category_2 = IntegerField()
    item_category_3 = IntegerField()
    item_category_4 = IntegerField()
    item_category_5 = IntegerField()
    item_id_1 = IntegerField()
    item_id_2 = IntegerField()
    item_id_3 = IntegerField()
    item_id_4 = IntegerField()
    item_id_5 = IntegerField()
    item_num_1 = IntegerField()
    item_num_2 = IntegerField()
    item_num_3 = IntegerField()
    item_num_4 = IntegerField()
    item_num_5 = IntegerField()
    team_class = IntegerField()
    team_stadium_id = IntegerField()

    class Meta:
        table_name = 'team_stadium_class_reward'
        indexes = (
            (('team_stadium_id', 'class_reward_type'), False),
        )

class TeamStadiumEvaluationRate(BaseModel):
    id = IntegerField()
    proper_rank = IntegerField()
    proper_type = IntegerField()
    rate = IntegerField()

    class Meta:
        table_name = 'team_stadium_evaluation_rate'
        indexes = (
            (('proper_type', 'proper_rank'), True),
        )
        primary_key = CompositeKey('proper_rank', 'proper_type')

class TeamStadiumRaceResultMotion(BaseModel):
    character_id = IntegerField(index=True)
    draw_1 = IntegerField()
    draw_2 = IntegerField()
    draw_3 = IntegerField()
    draw_4 = IntegerField()
    draw_5 = IntegerField()
    lose_1 = IntegerField()
    lose_2 = IntegerField()
    lose_3 = IntegerField()
    lose_4 = IntegerField()
    lose_5 = IntegerField()
    position_y = IntegerField()
    win_1 = IntegerField()
    win_2 = IntegerField()
    win_2_position_y = IntegerField()
    win_3 = IntegerField()
    win_3_position_y = IntegerField()
    win_4 = IntegerField()
    win_4_position_y = IntegerField()
    win_5 = IntegerField()

    class Meta:
        table_name = 'team_stadium_race_result_motion'
        primary_key = False

class TeamStadiumRank(BaseModel):
    item_category = IntegerField()
    item_id = IntegerField()
    item_num = IntegerField()
    team_max_value = IntegerField()
    team_min_value = IntegerField()
    team_rank = IntegerField()
    team_rank_group = IntegerField()

    class Meta:
        table_name = 'team_stadium_rank'

class TeamStadiumRawScore(BaseModel):
    condition_type = IntegerField(index=True)
    condition_value_1 = IntegerField()
    condition_value_2 = IntegerField()
    priority = IntegerField()
    race_score_name_id = IntegerField(index=True)
    score = IntegerField()
    sort_order = IntegerField()

    class Meta:
        table_name = 'team_stadium_raw_score'

class TeamStadiumScoreBonus(BaseModel):
    condition_type = IntegerField(index=True)
    condition_value_1 = IntegerField()
    condition_value_2 = IntegerField()
    priority = IntegerField()
    score_rate = IntegerField()

    class Meta:
        table_name = 'team_stadium_score_bonus'

class TeamStadiumStandMotion(BaseModel):
    character_id = IntegerField()
    motion_set = IntegerField()
    position = IntegerField()
    position_x = IntegerField()
    race_dress_id = IntegerField()
    rotation = IntegerField()
    type = IntegerField()

    class Meta:
        table_name = 'team_stadium_stand_motion'
        indexes = (
            (('character_id', 'type'), False),
        )
        primary_key = False

class TeamStadiumSupportText(BaseModel):
    max_bonus = IntegerField()
    min_bonus = IntegerField()
    type = IntegerField(index=True)

    class Meta:
        table_name = 'team_stadium_support_text'

class TextData(BaseModel):
    category = IntegerField()
    id = IntegerField()
    index = IntegerField()
    text = TextField()

    class Meta:
        table_name = 'text_data'
        indexes = (
            (('category', 'index'), True),
        )
        primary_key = CompositeKey('category', 'index')

class TimezoneData(BaseModel):
    end_hour = TextField()
    priority = IntegerField()
    start_hour = TextField()
    timezone = AutoField()

    class Meta:
        table_name = 'timezone_data'

class Topics(BaseModel):
    index = IntegerField()
    start_date = TextField()
    type = IntegerField(index=True)
    value = IntegerField()

    class Meta:
        table_name = 'topics'

class TrainedCharaTradeItem(BaseModel):
    trade_item_category = IntegerField()
    trade_item_id = IntegerField()
    trade_item_num = IntegerField()
    trained_chara_rank = IntegerField(unique=True)

    class Meta:
        table_name = 'trained_chara_trade_item'

class TrainingCuttCharaData(BaseModel):
    chara_id = IntegerField()
    chara_num = IntegerField()
    command_id = IntegerField()
    prop_target = IntegerField()
    sub_id = IntegerField()
    target_list_index = IntegerField()
    target_timeline = IntegerField()

    class Meta:
        table_name = 'training_cutt_chara_data'
        indexes = (
            (('command_id', 'sub_id'), False),
        )

class TrainingCuttData(BaseModel):
    chara_num = IntegerField()
    command_id = IntegerField()
    cutt_index = IntegerField()
    sub_id = IntegerField()
    success_flg = IntegerField()
    target_chara_index = IntegerField()
    target_value = IntegerField()

    class Meta:
        table_name = 'training_cutt_data'
        indexes = (
            (('command_id', 'sub_id'), False),
        )
        primary_key = False

class TutorialGuideData(BaseModel):
    group_id = IntegerField(index=True)
    image_index = IntegerField()
    page_index = IntegerField()

    class Meta:
        table_name = 'tutorial_guide_data'
        indexes = (
            (('group_id', 'page_index'), True),
        )

