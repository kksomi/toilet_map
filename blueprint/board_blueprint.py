from flask import Blueprint, render_template, session, request
from functools import wraps
import time
from database import board_dao

APIKEY = '5db49510eb17bbd4b25077eb2990c24f'

board_blue=Blueprint('board',__name__)

@board_blue.route('/board_map')
def board_map():
    content_list = board_dao.getlocation()
    #TODO
    # for c in content_list:
    # 	print(c)
    html = render_template('board/board_map.html',content_list=content_list, APIKEY=APIKEY)
    return html


@board_blue.route('/search')
def search_map():
    q = request.args.get('search')
    content_list = board_dao.getlocation()
    content_list = list(filter(lambda x:q in x['TNAME'], content_list))
    #                                   ^^^^^^^^^^^^^^^
    #                                   이 부분을 수정하면 됩니다!
    #                                   주소로 검색하고 싶다면...
    #                                   q in x['ADDR_DONG']
    #                                   으로 하시면 됩니다. 동시에 검색하고 싶다면
    #                                   q in x['ADDR_DONG'] or q in x['TNAME']
    for c in content_list:
        print(c)
    html = render_template('board/board_search.html',content_list=content_list, APIKEY=APIKEY, search=q)
    return html


@board_blue.route('/board_map/<toilet_idx>')
def toilet_info(toilet_idx):
    content_list=board_dao.gettoiletidx(toilet_idx)
    html=render_template('board/board_toiletinfo.html',content_list=content_list)
    return html
# @board_blue.route('/board_custom_result', methods=['post'])
# def board_custom_result() :
#     #사용자가 입력한 데이터를 가져온다.
#     course_loc = request.values.get('cafe_loc')
#     data_list=board_dao.loadCoursefoodInfoData(course_loc)
#     cafe_list=board_dao.loadCoursecafeInfoData(course_loc)
#     activity_list=board_dao.loadCourseactivityInfoData()
#     html = render_template('board/board_custom_result.html',data_list=data_list,cafe_list=cafe_list,activity_list=activity_list)
#     return html

@board_blue.route('/board_review')
def board_review() :
    html = render_template('board/board_review.html')
    return html