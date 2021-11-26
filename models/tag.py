# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tag(models.Model):
    _name = 'lab3.tag'
    _description = '標籤'

    name = fields.Char('標籤名',required=True)
    # 多對多(Many2many，參數: ['對方資料表','多對多參考表_rel','我方_id','對方_id','說明'])
    movie_ids = fields.Many2many('lab3.movie', 'lab3_movie_tag_rel', 'tag_id', 'movie_id', '電影')


