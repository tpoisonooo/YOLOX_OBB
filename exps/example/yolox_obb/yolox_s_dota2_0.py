#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import OBBExp as MyExp


class Exp(MyExp):
    def __init__(self):
        super().__init__()
        self.dataset_config="configs/datasets/dota20.yaml"
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
        # -----train config-------#
        self.warmup_epochs=1
        self.basic_lr_per_img = 0.01 / 64
        self.max_epoch = 80
        self.no_aug_epochs = 10
        # -----train config-------#
        self.no_eval = True
        self.copy_paste_prob = 1.0
        self.mosaic_prob = 1.0
        self.mixup_prob = 0.0 # it isn't suitable for remote images
        self.enable_resample = True # for resampling samples
        # enable debug which allow user to debug aug images
        # ignore images which exists horizontal labels, 
        # the rotated aug will not implement the classes by adding this item
        self.aug_ignore = ['roundabout', 'storage-tank'] 
        # ignore images which has no labels, which ensure each train contains labels
        self.empty_ignore = True

        self.test_conf = 0.05
        self.use_trig_loss = True # use extra angle l1 loss
        self._get_data_info(self.dataset_config)
