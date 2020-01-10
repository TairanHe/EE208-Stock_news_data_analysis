# EE208-Stock_news_data_analysis

I'm Liu.

###get_url.py: 
对于每支股票，获取在百家号上三页共三十个新闻

###init_url: 
为文件夹，以txt格式,股票编号为名称，储存上述新闻网址，例：“init_url/000034.txt”


###get_img_and_article.py:
对于每支股票所爬取的每个新闻，检测是否有图片，对于存在相关图片的网址
                        保留其标题，内容，图片三个部分
                        
###img_article: 
为文件夹，在其内部，每支股票以编号对应一个文件夹，该文件夹中包含新闻网址的内容标题与图片
例："img_article/000034/0/0.jpg" "img_article/000034/1/1_content.txt"

注：在content中，第一行为标题，第二号空，第三行开始内容
