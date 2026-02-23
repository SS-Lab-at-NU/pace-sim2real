# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg
from sslab_extensions.simulation.actuators import DelayedPDActuatorCfg

import subprocess
import os 

##
# Configuration
##

JOINT_ORDER = [
    "bl_hx", "br_hx", "fl_hx", "fr_hx", 
    "bl_hy", "br_hy", "fl_hy", "fr_hy",
    "bl_kn", "br_kn", "fl_kn", "fr_kn",
]

HUSKY_B_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        # usd_path=f"{'/workspace' if os.path.exists('/workspace') else subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()}/sslab-robots/husky_beta/usd/huskyb_full/huskyb_full.usd",
        usd_path=f"/home/arjun/Documents/sslab_isaaclab/sslab-robots/husky_beta/usd/huskyb_full/huskyb_full.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=1
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.55),
        joint_pos={
            "[fb]l_hx": 0.0,  # all left frontal hip joints
            "[fb]r_hx": 0.0,  # all left frontal hip joints
            "f[lr]_hy": 0.698132,  # all front sagittal hip joints
            "b[lr]_hy": 0.698132,  # all back sagittal hip joints
            "f[lr]_kn": 0.4,  # all front knee joints
            "b[lr]_kn": 0.4,  # all back knee joints
        },
        joint_vel={".*": 0.0},
    ),
    actuators={
        "frontal_hip": DelayedPDActuatorCfg(
            joint_names_expr=[".*_hx"],
            effort_limit=9.9,
            velocity_limit=3.0,
            stiffness=35.0,
            damping=1.0,
            armature=0.01,
            friction=0.04,
            min_delay=0,  # physics time steps (min: 2.0*0=0.0ms)
            max_delay=4,  # physics time steps (max: 2.0*4=8.0ms)
        ),
        "sagittal_hip": DelayedPDActuatorCfg(
            joint_names_expr=[".*_hy"],
            effort_limit=9.9,
            velocity_limit=3.0,
            stiffness=35.0,
            damping=1.0,
            armature=0.01,
            friction=0.04,
            min_delay=0,  # physics time steps (min: 2.0*0=0.0ms)
            max_delay=4,  # physics time steps (max: 2.0*4=8.0ms)
        ),
        "knees": DelayedPDActuatorCfg(
            joint_names_expr=[".*_kn"],
            effort_limit=10.6,
            velocity_limit=3.0,
            stiffness=45.0,
            damping=1.5,
            armature=0.01,
            friction=0.04,
            min_delay=0,  # physics time steps (min: 2.0*0=0.0ms)
            max_delay=4,  # physics time steps (max: 2.0*4=8.0ms)
        ),
    },
)

"""Configuration for the Husky Beta robot."""
