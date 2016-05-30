#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# @file content.py
# @brief read the file for the presentation
# @author scusjs@foxmail.com
# @version 0.1.00
# @date 2015-05-10

import locale
locale.setlocale(locale.LC_ALL, '')


class Content:
    def __init__(self, file_path):
        self.path = file_path
        file_object = 0
        with open(file_path, 'r') as file_object:
            self.__read_presentation(file_object)

    def __read_presentation(self, file_object):
        file_list = file_object.readlines()
        content_list = []
        page_list = []
        page_attribute = []
        content_attribute = []
        for i in range(0, len(file_list)):
            if file_list[i].find("#") == 0:
                continue
            if file_list[i].find("page") == 0:
                if len(page_list) != 0:
                    content_list.append(
                        {"content": page_list, "attribute": page_attribute})
                page_list = []
                page_attribute = []
                attribute = file_list[i].strip().split(":")[1]
                attribute = attribute.split(",")
                for each in attribute:
                    page_attribute.append(each)
            elif file_list[i].find("content") == 0:
                content_attribute = []
                attribute = file_list[i].strip().split(":")[1]
                attribute = attribute.split(",")
                for each in attribute:
                    content_attribute.append(each)
            elif file_list[i] == '\n':
                continue
            else:
                content = file_list[i][:-1]
                page_list.append(
                    {"content": content, "attribute": content_attribute})

        if len(page_list) != 0:
            content_list.append(
                {"content": page_list, "attribute": page_attribute})
        self.content_list = content_list

    def get_content_list(self):
        return self.content_list


if __name__ == "__main__":
    ct = Content("./example/example")
    print(ct.get_content_list())
