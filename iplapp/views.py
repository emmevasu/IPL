from django.shortcuts import render
from django.http import HttpResponse

from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib import pylab 
from matplotlib import pyplot as plt 
from pylab import *
import PIL, PIL.Image
from io import BytesIO, StringIO
import io
import urllib,base64
from django.template.loader import get_template

# Create your views here
# player_names=[]
# player_scores=[]

def IplTopScorer(requests,num):
    

    page=urlopen('https://www.iplt20.com/stats/2020/most-runs')

    soup=BeautifulSoup(page,'html.parser')

    lead=soup.findAll('div' ,attrs={'class':'stats-table'})
    player=lead[0].findAll('span',attrs={'class':'top-players__last-name'})
    score=lead[0].findAll('td',attrs={'class':'top-players__r is-active'})
        # player[:i].text.strip()
    player_names=[]

    player_scores=[]

    Top_Players=zip(player_names,player_scores)
    
    

    for i in range(0,int(num)):

            # player=lead[0].findAll('span',attrs={'class':'top-players__last-name'})

        player_names.append(player[i].text.strip())

            # score=lead[0].findAll('td',attrs={'class':'top-players__r is-active'})

        player_scores.append(score[i].text.strip())

        # player_names.save()
        # player_scores.save()

    return render(requests,'details.html',{'data':Top_Players})


def Input(re):
    return render('input.html')


# def graph(requets):
#     plt.bar(['a','b'],[10,20])
#     fig=plt.gcf()
#     buf=io.BytesIO()
#     fig.savefig(buf,format='png')
#     buf.seek(0)
#     strin=base64.b64decode(buf.read())
#     url=urllib.parse.quote(strin)
#     context={'data':url}
#     template = get_template('image.html')
#     html = template.render(context=context)
#     # return HttpResponse (url.show(), content_type="Image/png")
#     return render(requets,'image.html',context)



    # def getimage(request):
    #     # domain = request.data["domain"]
    #     # function = request.data["function"]
    #     # x = arange(domain[0], domain[1], 0.01)
    #     # s = function
    #     plot(player_names, player_scores)


    #     xlabel('xlabel(X)')
    #     ylabel('ylabel(Y)')
    #     title('Simple Graph!')
    #     grid(True)

    #     # Store image in a string buffer
    #     buffer = StringIO()
    #     canvas = pylab.get_current_fig_manager().canvas
    #     canvas.draw()
    #     pilImage = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    #     pilImage.save(buffer, "PNG")
    #     pylab.close()

    #     # Send buffer in a http response the the browser with the mime type image/png set
    #     return HttpResponse(buffer.getvalue(), mimetype="image/png")
    # def ima(requets):
        # plt.bar(player_names,player_scores)
        # fig=plt.gcf()
        # buf=io.BytesIO()
        # fig.savefig(buf,format='png')
        # buf.seek(0)
        # strin=base64.b64decode(buf.read())
        # url=urllib.parse.quote(strin)
        # return render(requets,'image.html',{'data':url})