from zhihu_user_info_spider.proxypool.ProxyPool import Proxy_pool
from zhihu_user_info_spider.threadpool.ThreadPool import ThreadPool
import time
from zhihu_user_info_spider.util.Utils import *
import requests

threadPool = ThreadPool(20)
spider_util = ()
proxy = Proxy_pool()
url = "https://www.zhihu.com/api/v4/members/aton/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&offset=0&limit=20"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "x-zse-93": "101_3_2.0",
    "x-zse-96": "2.0_aMtBgg98SR2fcTYqT9YqnqrqFwFYUCNq8_N0FDuBb7tf",
    "x-zst-81": "3_2.0ae3TnRUTEvOOUCNMTQnTSHUZo02p-HNMZBO8YD70rTtuQ0tqK6P0Ei9y-LS9-hp1DufI-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_Ie8FL7AtqM6O1VDQyQ6nxrRPCHukMoCXBEgOsiRP0XL2ZUBXmDDV9qhnyTXFMnXcTF_ntRueThHtK3qN8EUXxaBwYMQS8Ir9_OqHXqhwypq29tJwLjJXsDBpfs8Nm3gr_jhLPv0VZpCHMkAp1iwtpswN0KLt0VrUG-qFp3hoVDJH9nCN1reHV1gLyiBwCQ7xqsqompCeLmTVq6gUKVDS8HDC8qvS1IqOGUrNs6cN12uVKshoLeJS1fJxm4qfzWG_mwDS99Dx1m8YygcpqcRtxSLoBB_2Barc_hBXfzUxKB93OhbH_ChNxP920fLL9wgV0QgtK2ioCEge8fJeB-qpMhqV8x9gKDbOOQgpY89wmuwHL2JUC",
    # "cookie": '_zap=75aabf48-9f5e-4bd5-8b45-5c86ea629af9; d_c0="AIAeliYS1hKPTj048FpaXUnf7FYUF_C1nec=|1616383700"; __snaker__id=3VwOLSmmOn9h1Tly; _9755xjdesxxd_=32; _xsrf=fsLkUGprrmu95wo9flAuLgCcD0pqeEEE; YD00517437729195%3AWM_TID=nGgl5HPMg2dEEFEVVANrjRr4Se9oUP93; __utma=51854390.853983904.1625210375.1625210375.1625210375.1; __utmz=51854390.1625210375.1.1.utmcsr=zhuanlan.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/76389233; __utmv=51854390.100--|2=registration_date=20180809=1^3=entry_date=20180809=1; tshl=; q_c1=9c117b7af8ca4c6fa0be804508df1309|1632389114000|1625210374000; _ga=GA1.2.853983904.1625210375; _gid=GA1.2.2015699954.1632799732; cap_id="OTc0NjkyOTc0YTg0NGQ3OWI3Mzg5NWI3NWYzNzEwZDE=|1632801683|9fb5c7b13ff72b321ba3b5d83714089d661ff8a6"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1632801792,1632801805,1632801848,1632810595; SESSIONID=0wFhyyZEIvjakSqntPYUJqAVVBWaDXLUw1Jc53LkQGO; JOID=Vl4RBknAAcpdf8YlecD1Fm43ejdq8nSNMgC9fT2PdaI9E5NWFbu0nj17xiZ_KcvxggWY33yyKl3U2wknhXyktss=; osd=W1kUBELNBs9fdMsifML-G2kyeDxn9XGPOQ26eD-EeKU4EZhbEr62lTB8wyR0JMz0gA6V2HmwIVDT3gssiHuhtMA=; anc_cap_id=b18b1650ddce47d2bc51639865b0c86c; YD00517437729195%3AWM_NI=tTAxY6SGToiHVc%2BbhueHk2wjzA5l%2BdoikMEwK5VHUUFv%2BHS1pgOvM6smipmuT3UBfHE5%2F5bUElM2PUDG2xQWgylLk8rHh0e4ROZ8Tb6qHaVVssQEQNTz0zMFDCF18nkab0s%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb2c87c83f58c8bc749a39e8bb7c84f839e8eaef18086b2aeb4ee63abf599a5c12af0fea7c3b92ab88c8f99dc3e91999c90ec4496bde583eb7fa798a5d3f662ba9ffb8daa70adb7a5aec87d89eb9aa9d85f86aae5a9d23bb4b98197d03eb1b3a791f07f98ed9ba3e54487ebe1d6e15f87b483d3d35f8899fe99d45da5a7a4adea34b298a8d1e840929196d9d76af6af8882d55eb1ad9fa6d44698a6009bd04e889d8ad2bb66a9bfaed1f237e2a3; capsion_ticket="2|1:0|10:1632812961|14:capsion_ticket|44:NDNmODJjNjkwYTc1NGE4NjhmZjNkMGM5MWI0MWIyMzY=|832beb236d70695fa3af586f102d089b804eac15d040716247e8e081b243aec1"; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1632816053; captcha_session_v2="2|1:0|10:1632816053|18:captcha_session_v2|88:SlZlM3dheGZoVEJ2VDg5SkdaZzB1VUswaS9keWg4SUZLd0IxR1piZXFqQlNpY282QTRIU1U3Uml6TjJWNHB4Qw==|319eacf7beef285cc102bacc39feaf8c9cdd1acfe7d2bfecd120f3da81f546c7"; gdxidpyhxdE=Rvq9L3h6B3Jmj%2Fr4EEuGEPUhfcE%2Fhtl5HM0i4amZab6CuR1hnCCLe%2BIiLWah5okZEWT812p8E1ERREW7zOQdSM78GBsmpfOdvkw%5C4VzxWCgrYzfjMxYI6g41svTX5o2HcyeZV6aqYb9kLWj0aWa5u4DwcnNsRsctef5s1k9OKjN9%5COKw%3A1632816954182; captcha_ticket_v2="2|1:0|10:1632816064|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfTUFxNjl3MjRENWJEZTJWTTdoUUUtT3dnR2NOcXN2OGhQT0Z5cmpBa3lnMXhYbjU5SzI2X1pIQVp1Q2E2aFNxQm1pVjBxQXMxZ3BfZ2FDSnNZd21nQzdtSW11Sk1ZakM5cmwyUmw0aDVWaFdNSS1MZTBCc01uS3hTLVBBdVRQb1hacEZ0c200UlpDRlI2Tno1ZWtCOC1FVlJiY0pMbkFtU0JJbXgyQlluR1ZyUm9BOGNTZVBWLTJxLjBfRzY5QTl4MmlSbEdUVW1DSU9OWmZUOG5BcWk0ZVlvQUUxTmgxalU5czQteEE1ZnhUWXA5aWlpblJNckRqaU9uTmNPSjZHcHg2ZXVMa0Mxd19NWkxzdXBCSVc1dWtZN1JoNi1pVy4yRHhqMHByLXJrUEtNZV9pcVRqSi1zSEZ4V3Q2cjZjbkpsdjlZTHFoaXpZLlJyYjhteWxtaUw4d2VLLXJvUE9PSWZ0T3BpTW40LlZ6UFBIeFRtRXRSRUZPYWlueUdVMC5CSmV3c1RQRjZwYjhRRDBpaTEyTHRHYU90MVlURzJkbXp1RHRRZHhVSEZtb0ZXaTkydUtGSkhfME5XNjJETV9JUzdjZW5hVC1OTjJ6TVhiNXdxaThVLXZtQUVFaFE4Z0dXSjZlLnBYNldfUGw2UmVaelpjSC54N2pFemJwMyJ9|25b17a338eb02a2e507afb0948ae99ed6fcfd7c54f7f8e9ff85609ef791e0ce1"; KLBRSID=c450def82e5863a200934bb67541d696|1632816064|1632807189; z_c0="2|1:0|10:1632816064|4:z_c0|92:Mi4xZEdPQkN3QUFBQUFBZ0I2V0poTFdFaVlBQUFCZ0FsVk53QmxBWWdBdTFUOE9CMU9ucEI2eWlWOWZkVzVaVlBzcHBn|38e183829aa00250ba874179b87c3054dbc8d18277e82c5f4cbb1c4d4bdfb8b2"'
    # "cookie": '_zap=75aabf48-9f5e-4bd5-8b45-5c86ea629af9; d_c0="AIAeliYS1hKPTj048FpaXUnf7FYUF_C1nec=|1616383700"; __snaker__id=3VwOLSmmOn9h1Tly; _9755xjdesxxd_=32; _xsrf=fsLkUGprrmu95wo9flAuLgCcD0pqeEEE; YD00517437729195%3AWM_TID=nGgl5HPMg2dEEFEVVANrjRr4Se9oUP93; __utma=51854390.853983904.1625210375.1625210375.1625210375.1; __utmz=51854390.1625210375.1.1.utmcsr=zhuanlan.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/76389233; __utmv=51854390.100--|2=registration_date=20180809=1^3=entry_date=20180809=1; tshl=; q_c1=9c117b7af8ca4c6fa0be804508df1309|1632389114000|1625210374000; _ga=GA1.2.853983904.1625210375; _gid=GA1.2.2015699954.1632799732; cap_id="OTc0NjkyOTc0YTg0NGQ3OWI3Mzg5NWI3NWYzNzEwZDE=|1632801683|9fb5c7b13ff72b321ba3b5d83714089d661ff8a6"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1632801792,1632801805,1632801848,1632810595; SESSIONID=0wFhyyZEIvjakSqntPYUJqAVVBWaDXLUw1Jc53LkQGO; JOID=Vl4RBknAAcpdf8YlecD1Fm43ejdq8nSNMgC9fT2PdaI9E5NWFbu0nj17xiZ_KcvxggWY33yyKl3U2wknhXyktss=; osd=W1kUBELNBs9fdMsifML-G2kyeDxn9XGPOQ26eD-EeKU4EZhbEr62lTB8wyR0JMz0gA6V2HmwIVDT3gssiHuhtMA=; anc_cap_id=b18b1650ddce47d2bc51639865b0c86c; YD00517437729195%3AWM_NI=tTAxY6SGToiHVc%2BbhueHk2wjzA5l%2BdoikMEwK5VHUUFv%2BHS1pgOvM6smipmuT3UBfHE5%2F5bUElM2PUDG2xQWgylLk8rHh0e4ROZ8Tb6qHaVVssQEQNTz0zMFDCF18nkab0s%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb2c87c83f58c8bc749a39e8bb7c84f839e8eaef18086b2aeb4ee63abf599a5c12af0fea7c3b92ab88c8f99dc3e91999c90ec4496bde583eb7fa798a5d3f662ba9ffb8daa70adb7a5aec87d89eb9aa9d85f86aae5a9d23bb4b98197d03eb1b3a791f07f98ed9ba3e54487ebe1d6e15f87b483d3d35f8899fe99d45da5a7a4adea34b298a8d1e840929196d9d76af6af8882d55eb1ad9fa6d44698a6009bd04e889d8ad2bb66a9bfaed1f237e2a3; capsion_ticket="2|1:0|10:1632812961|14:capsion_ticket|44:NDNmODJjNjkwYTc1NGE4NjhmZjNkMGM5MWI0MWIyMzY=|832beb236d70695fa3af586f102d089b804eac15d040716247e8e081b243aec1"; tst=r; gdxidpyhxdE=Rvq9L3h6B3Jmj%2Fr4EEuGEPUhfcE%2Fhtl5HM0i4amZab6CuR1hnCCLe%2BIiLWah5okZEWT812p8E1ERREW7zOQdSM78GBsmpfOdvkw%5C4VzxWCgrYzfjMxYI6g41svTX5o2HcyeZV6aqYb9kLWj0aWa5u4DwcnNsRsctef5s1k9OKjN9%5COKw%3A1632816954182; captcha_session_v2="2|1:0|10:1632816437|18:captcha_session_v2|88:S2sycVpRN0dEbFF5RWtmUVdCMGdiK1V6dWI4eGZodCtjam03ckxZdCt5aE41UHZDeTJYa3JvYkNtYjNaTEZGMg==|cc325daca3ae3a02ac6bbcb73a9640ef1f50373b8384a96ce420ac9448b0879e"; captcha_ticket_v2="2|1:0|10:1632816463|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfR1ljOVRBVlBkZUJCWmF2dTZPenliVl9DNE5pUGZ2LkV1ODZQQVNEQ1NZaTRVenhMT3JhU3F6NlplcTUwbm95Lkc2VUIxS3p2WU9weS5haFNpVEtEWnJvejVIY1Etc1Z3eTVWdm54ckFXQnd4LS5YbXRFMDkuajluZkliTFMxV19BQlF6UTZBQmdkTDVleUxjczdnNmtLWmM4UEJ0QWhJOUNaTnUtT2p6V08uV0pDX1NvUnplLURjcTBDcl80N2pBQ3k4WGNqUE5jcGxvLUY2VFdEV2hLVWkuNGxnT19TTmhWVGxnX1RwRWRIUUFaYWRhVW5BU3pYZ0ViQzlLVHJodC41cG9iNkZ6NF8tUW94Qm85bjZONjYydWUtOTcyMVVpcXNCelpWX3Y0WEVjV1VLLk51VEJodjlTazhTVWY4Q1M2bmxyZEFrRkY3b0xaaC44TFhOWTVYcnhwTjRHR0s1eWNlVlQ3RnZtRXAyRC0tdmJjZWhWX1ZZSVJ6NTAtQTd3YzBCc1FuYzVCR0k2RjVLYTcyTDdwbnUyTVh0ZjEuU0dxdGQucVZtd2xCNnhyY2s0U2ZSaDg0MkdmNDFlNDFRZ0daSEI1Y0V2dXdFTmdXT1dNMVdJaVFlWGVRVG1CYmFycG1LLnl0YnUtUmNvYlhaR0dUNFh3Ry5uQTlJMyJ9|3e7d534c93063a4fb58c5e2f13cb2ac19ba049010342b200a3f9b84e72d0d4fc"; z_c0="2|1:0|10:1632816464|4:z_c0|92:Mi4xX2FxR01nQUFBQUFBZ0I2V0poTFdFaVlBQUFCZ0FsVk5VQnRBWWdERElYSEdUSkZNdWVsRzRORmM2UXhQOGF0Vjd3|92816989143249b5c16bf43504d12ecdb7e2f69962b6b3fe977b7a774492f48e"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1632816465; KLBRSID=c450def82e5863a200934bb67541d696|1632816467|1632807189'
}

cookie='_zap=75aabf48-9f5e-4bd5-8b45-5c86ea629af9; d_c0="AIAeliYS1hKPTj048FpaXUnf7FYUF_C1nec=|1616383700"; __snaker__id=3VwOLSmmOn9h1Tly; _9755xjdesxxd_=32; _xsrf=fsLkUGprrmu95wo9flAuLgCcD0pqeEEE; YD00517437729195%3AWM_TID=nGgl5HPMg2dEEFEVVANrjRr4Se9oUP93; __utma=51854390.853983904.1625210375.1625210375.1625210375.1; __utmz=51854390.1625210375.1.1.utmcsr=zhuanlan.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/76389233; __utmv=51854390.100--|2=registration_date=20180809=1^3=entry_date=20180809=1; tshl=; q_c1=9c117b7af8ca4c6fa0be804508df1309|1632389114000|1625210374000; _ga=GA1.2.853983904.1625210375; _gid=GA1.2.2015699954.1632799732; cap_id="OTc0NjkyOTc0YTg0NGQ3OWI3Mzg5NWI3NWYzNzEwZDE=|1632801683|9fb5c7b13ff72b321ba3b5d83714089d661ff8a6"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1632801792,1632801805,1632801848,1632810595; SESSIONID=0wFhyyZEIvjakSqntPYUJqAVVBWaDXLUw1Jc53LkQGO; JOID=Vl4RBknAAcpdf8YlecD1Fm43ejdq8nSNMgC9fT2PdaI9E5NWFbu0nj17xiZ_KcvxggWY33yyKl3U2wknhXyktss=; osd=W1kUBELNBs9fdMsifML-G2kyeDxn9XGPOQ26eD-EeKU4EZhbEr62lTB8wyR0JMz0gA6V2HmwIVDT3gssiHuhtMA=; anc_cap_id=b18b1650ddce47d2bc51639865b0c86c; gdxidpyhxdE=M8Kl7HpyqGz2nfgU2cIeHv4U1YyioTgOwPPcKP3UvOHn%5Ca21AdD89z%5C6gQ4h%5CKYicVX99zQA19tgSlIPbIa2aE6n%2BaEeGMTS3mOZ44%2FqysjNNs1Y%2FGzIZDaIOY9%5CN0Usk7fv9xlY9o2miWGlOnAABRtTx42xq8gWCoI2Oto7Q2PdNp4l%3A1632813750387; YD00517437729195%3AWM_NI=tTAxY6SGToiHVc%2BbhueHk2wjzA5l%2BdoikMEwK5VHUUFv%2BHS1pgOvM6smipmuT3UBfHE5%2F5bUElM2PUDG2xQWgylLk8rHh0e4ROZ8Tb6qHaVVssQEQNTz0zMFDCF18nkab0s%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb2c87c83f58c8bc749a39e8bb7c84f839e8eaef18086b2aeb4ee63abf599a5c12af0fea7c3b92ab88c8f99dc3e91999c90ec4496bde583eb7fa798a5d3f662ba9ffb8daa70adb7a5aec87d89eb9aa9d85f86aae5a9d23bb4b98197d03eb1b3a791f07f98ed9ba3e54487ebe1d6e15f87b483d3d35f8899fe99d45da5a7a4adea34b298a8d1e840929196d9d76af6af8882d55eb1ad9fa6d44698a6009bd04e889d8ad2bb66a9bfaed1f237e2a3; capsion_ticket="2|1:0|10:1632812961|14:capsion_ticket|44:NDNmODJjNjkwYTc1NGE4NjhmZjNkMGM5MWI0MWIyMzY=|832beb236d70695fa3af586f102d089b804eac15d040716247e8e081b243aec1"; tst=r; captcha_session_v2="2|1:0|10:1632813185|18:captcha_session_v2|88:L25GSjEvb0l3SE1NbE16aTRUQy9aTHY3TjlwUWk0QVNjNGJ2Q0c0blM2SVZCVkNzWjh4dUlMNFhMUGdJUmRzbQ==|cf7f3adf0ea0d6c6b489abb15142d239f8828e3600b93360c3ab5b79a45c2c08"; captcha_ticket_v2="2|1:0|10:1632813202|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfNkcyWWNsLnZXeUNCRVJJUVNGUW1QLmhhOC5Na1lUWGd3Z2I5aU15b0IwQnRsVzdUSGRQemgteHlBenRZVkV3RVBaXzhRU25mWEl1dVJiWHJLLkVpSlZRVjQ5SVRnaGdzcHhnSmhrY2lEc3VUZlBvaHhyWW1EaEc5Z2ZTT1dhRkdnU2J4dUpQa1ZkckhZTnRkRFFSMFM4TzBlUktHb1FjZEFyVzh0VVVwNnhJbWVuWl9wV3JLdFYwOHlwaTZTRktILUIuVk1IdktzQmFYMXVFTGh2S2s3RE96ZkdhUThoS2RkQUlUc2tUSS5lWlJQSy56TEtvb3ZzU2lXd1lmZ2lRUmFLX1lvZjU4NlkxZm04dUpjMjVDaWRPbENTNWFkdnY2S1o4MEx1X29KbUJQaThGeTZjSlZrRElyei5WZnRfVy5QdFN3eWRUWWRudFBKU19ZMlB0N0oxUExvMF84czZ3TWVBQmQ2MVJ0QTlVdEhsWTJObUpUVk1xendkekpaN01zWFFHQzhLVkZWazFZQm9fSnlTU1dKV2FiTmFqR1Vta2gxLWIwR0JiWi5EWS4tQVlyLmRJdlJ5N05ES0xKNTlsb3ZPTWM2cVpfTEtjUUFMQ01BbE16YXRXaXFDN3V1Tm05N2xJNlhwcVpWQ3oyVkROUXRxSl9LcWxGNUtjMyJ9|80c8e8cb2c830f112fd2db4b50a2c767e0c1a4469922bc6d5b9a2f5431d21775"; z_c0="2|1:0|10:1632813203|4:z_c0|92:Mi4xX2FxR01nQUFBQUFBZ0I2V0poTFdFaVlBQUFCZ0FsVk5rdzVBWWdBZkhVeHpTX3VGano0US1Ic0NBRzVyWmt4aDVB|2e7a79a5c3ff59be1618573d139c36fce154ff6072e9d433eb9fbfcc408727d0"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1632813214; KLBRSID=c450def82e5863a200934bb67541d696|1632813228|1632807189'


def __random_header():
    headers = {
        "x-zse-93": "101_3_2.0",
        "x-zse-96": "2.0_aMtBgg98SR2fcTYqT9YqnqrqFwFYUCNq8_N0FDuBb7tf",
        "x-zst-81": "3_2.0ae3TnRUTEvOOUCNMTQnTSHUZo02p-HNMZBO8YD70rTtuQ0tqK6P0Ei9y-LS9-hp1DufI-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_Ie8FL7AtqM6O1VDQyQ6nxrRPCHukMoCXBEgOsiRP0XL2ZUBXmDDV9qhnyTXFMnXcTF_ntRueThHtK3qN8EUXxaBwYMQS8Ir9_OqHXqhwypq29tJwLjJXsDBpfs8Nm3gr_jhLPv0VZpCHMkAp1iwtpswN0KLt0VrUG-qFp3hoVDJH9nCN1reHV1gLyiBwCQ7xqsqompCeLmTVq6gUKVDS8HDC8qvS1IqOGUrNs6cN12uVKshoLeJS1fJxm4qfzWG_mwDS99Dx1m8YygcpqcRtxSLoBB_2Barc_hBXfzUxKB93OhbH_ChNxP920fLL9wgV0QgtK2ioCEge8fJeB-qpMhqV8x9gKDbOOQgpY89wmuwHL2JUC",
        "user-agent": spider_util.get_user_Agent()
    }
    return headers

def __random_cookie():
    header=__random_header()
    header["cookie"]=spider_util.get_cookie()
    return header

def get(i):
    # time.sleep(5)
    # print(i)
    # print("第"+str(i)+"个："+proxy.get_response(url=url, headers=headers,cookie=__random_cookie(), retry_count=20).text)
    print(__random_cookie())
    print(requests.get(url=url, headers=__random_cookie()).text)

def get1(i):
    print(str(i)+"\n")

def callback(message,status):
    print(message)

if __name__ == '__main__':
    for i in range(0, 10000):
        # print(i)
        # print(proxy.get_response(url=url, headers=headers, retry_count=20).text)
        # threadPool.run(func=get,args=(i,),callback=callback)
    # threadPool.close()
        # get1(i)
        get(i)