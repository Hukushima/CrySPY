#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import VASP
from . import QE
from ..IO import read_input as rin


def check_calc_files():
    if rin.calc_code == 'VASP':
        VASP.calc_files_vasp.check_input_vasp()
    elif rin.calc_code == 'QE':
        QE.calc_files_qe.check_input_qe()
    else:
        raise SystemExit('now only VASP or QE')


def next_stage(stage, work_path, *args):
    # args[0] <-- kpt_data
    # args[1] <-- current_ID
    if rin.calc_code == 'VASP':
        skip_flag, kpt_data = VASP.ctrl_job_vasp.next_stage_vasp(stage, work_path, args[0], args[1])
        return skip_flag, kpt_data
    elif rin.calc_code == 'QE':
        skip_flag, kpt_data = QE.ctrl_job_qe.next_stage_qe(stage, work_path, args[0], args[1])
        return skip_flag, kpt_data
    else:
        raise SystemExit('now only VASP or QE')


def collect(current_id, work_path):
    if rin.calc_code == 'VASP':
        opt_struc, energy, magmom, check_opt = \
            VASP.collect_vasp.collect_vasp(current_id, work_path)
    elif rin.calc_code == 'QE':
        opt_struc, energy, magmom, check_opt = \
            QE.collect_qe.collect_qe(current_id, work_path)
    else:
        raise SystemExit('now only VASP or QE')

    #---------- return
    return opt_struc, energy, magmom, check_opt


def next_struc(init_struc_data, next_id, work_path, *args):
    # args[0] <-- kpt_data
    if rin.calc_code == 'VASP':
        kpt_data = VASP.ctrl_job_vasp.next_struc_vasp(init_struc_data, next_id, work_path, args[0])
        return kpt_data
    elif rin.calc_code == 'QE':
        kpt_data = QE.ctrl_job_qe.next_struc_qe(init_struc_data, next_id, work_path, args[0])
        return kpt_data
    else:
        raise SystemExit('now only VASP or QE')


def clean_calc_files(work_path):
    if rin.calc_code == 'VASP':
        VASP.calc_files_vasp.clean_calc_files_vasp(work_path)
    elif rin.calc_code == 'QE':
        QE.calc_files_qe.clean_calc_files_qe(work_path)
    else:
        raise SystemExit('now only VASP or QE')
