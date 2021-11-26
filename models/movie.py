# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Movie(models.Model):
    _name = 'lab3.movie'
    _description = '電影'

    name = fields.Char('片名',required=True)
    mins = fields.Integer('片長')
    #多對多(Many2many，參數: ['對方資料表','多對多參考表_rel','我方_id','對方_id','說明'])
    tag_ids = fields.Many2many('lab3.tag', 'lab3_movie_tag_rel', 'movie_id', 'tag_id', '標籤名')

