# -*- coding: utf-8 -*-
"""
Created the 19/01/2023

@author: Sebastien Weber and N Tappy
"""
# Standard imports
from collections import OrderedDict
from typing import List, Dict

# 3rd party imports
import numpy as np


def find_scan_node(scan_node):
    """
    utility function to find the parent node of "scan" type, meaning some of its children (DAQ_scan case)
    or co-nodes (daq_logger case) are navigation axes
    Parameters
    ----------
    scan_node: (pytables node)
        data node from where this function look for its navigation axes if any
    Returns
    -------
    node: the parent node of 'scan' type
    list: the data nodes of type 'navigation_axis' corresponding to the initial data node


    """
    try:
        while True:
            if scan_node.attrs['type'] == 'scan':
                break
            else:
                scan_node = scan_node.parent_node
        children = list(scan_node.children().values())  # for data saved using daq_scan
        children.extend([scan_node.parent_node.children()[child] for child in
                         scan_node.parent_node.children_name()])  # for data saved using the daq_logger
        nav_children = []
        for child in children:
            if 'type' in child.attrs.attrs_name:
                if child.attrs['type'] == 'navigation_axis':
                    nav_children.append(child)
        return scan_node, nav_children
    except Exception:
        return None, []


def get_h5_attributes(self, node_path):
    """
        """
    node = self.get_node(node_path)
    attrs_names = node.attrs.attrs_name
    attr_dict = OrderedDict([])
    for attr in attrs_names:
        # if attr!='settings':
        attr_dict[attr] = node.attrs[attr]

    settings = None
    scan_settings = None
    if 'settings' in attrs_names:
        if node.attrs['settings'] != '':
            settings = node.attrs['settings']

    if 'scan_settings' in attrs_names:
        if node.attrs['scan_settings'] != '':
            scan_settings = node.attrs['scan_settings']
    pixmaps = []
    for attr in attrs_names:
        if 'pixmap' in attr:
            pixmaps.append(node.attrs[attr])

    return attr_dict, settings, scan_settings, pixmaps


def get_h5_data_from_node():
    pass


def extract_axis():
    pass


def verify_axis_data_uniformity():
    pass