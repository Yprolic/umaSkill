# -*- coding: utf-8 -*
from db.master_db import TextData, SkillData


class Skill:
    def __init__(self):
        pass

    def get_data_by_name(self, name):
        td = TextData.get(TextData.text == name)
        sd = SkillData.get_by_id(td.index)
        return sd


if __name__ == '__main__':
    skill = Skill()
    print(skill.get_data_by_name("長距離直線○").condition_1)
