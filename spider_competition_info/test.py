# 正文信息
specific_item_text = re.findall(
    '<div class="body-main main-wrap v-4-2">([\s\S]*?)<div class="footer-wrap v-4-2">',
    html).__getitem__(0)
# 右侧信息
specific_item_text_summary = re.findall(
    '<div class="sk-event-summary-box">([\s\S]*?)<div class="new-event4-1-box event-weixin-box">',
    html).__getitem__(0)
# 得到图片路径
specific_item_img_zz = u'<img[^>]+class=[^>]+>'
specific_item_img = re.findall(specific_item_img_zz, specific_item_text).__getitem__(0)
specific_item_imgurl_zz = u'src="(https://.*?)"'
specific_item_imgurl = re.findall(specific_item_imgurl_zz, specific_item_img).__getitem__(0)
# 得到竞赛信息!!!
specific_item_content = re.findall(
    '<div class="event4-1-detail-text-box text-body clearfix">([\s\S]*?)<div class="event4-1-detail-box v-4-9">',
    html).__getitem__(0)
# 得到发布者
specific_item_publisher_zz = u'<dd class="item-desc" title="(.*?)">'
specific_item_publisher = re.findall(specific_item_publisher_zz,
                                     specific_item_text_summary).__getitem__(0)
# 得到类型
specific_item_type_zz = u'类型<span class="title-desc">(.*?)</span>'
specific_item_type = re.findall(specific_item_type_zz, specific_item_text_summary).__getitem__(0)
# 得到报名费
specific_item_money_zz = u'报名费<span class="title-desc">(.*?)</span>'
specific_item_money = re.findall(specific_item_money_zz, specific_item_text_summary).__getitem__(0)
# 得到级别
specific_item_rank_zz = '级别.*?<span class="title-desc">([\s\S]*?)(.*?)</span>'
specific_item_rank = re.findall(specific_item_rank_zz, specific_item_text_summary)
# 得到参赛对象、报名时间、比赛时间
specific_item_participants_zz = u'<li class="new-event4-1-info-item clearfix">[^>]+<div class="info-content">[^>]+</div>'
specific_item_ParticipantsTime = re.findall(specific_item_participants_zz, specific_item_text_summary)
specific_item_participants_zz02 = u'<div class="info-content">[^>]+</div>'
specific_item_Participants = re.findall(specific_item_participants_zz02,
                                        specific_item_ParticipantsTime.__getitem__(0))
specific_item_time_signup = re.findall(specific_item_participants_zz02,
                                       specific_item_ParticipantsTime.__getitem__(1))
specific_item_time_play = re.findall(specific_item_participants_zz02,
                                     specific_item_ParticipantsTime.__getitem__(2))
# 得到竞赛类别
specific_item_category_zz = u'<div class="info-content clearfix">[^>]+<span class="fl item-prize">(.*?)</span>'
try:
    specific_item_category = re.findall(specific_item_category_zz,
                                        specific_item_text_summary).__getitem__(1)
except:
    specific_item_category = re.findall(specific_item_category_zz,
                                        specific_item_text_summary).__getitem__(0)

# print(specific_item_imgurl)
# # print specific_item_content
# print(specific_item_publisher)
# print(specific_item_type)
# print(specific_item_money)
# print(specific_item_rank)
# print(specific_item_ParticipantsTime)
# print(specific_item_Participants)
# print(specific_item_time_signup)
# print(specific_item_time_play)
# print(specific_item_category)
