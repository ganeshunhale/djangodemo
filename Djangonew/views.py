from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import pandas as pd
import os
def homepage(request):

    data={"name":"ganesh"}
    return render(request,"index.html",data)

# def aboutUs(request):
#         return HttpResponse("welcome")

# class  aboutUs(View):    
def aboutUs(request):
    try:
        # data = (request)
        print("dne")
        data={"name":"aboutus"}
        return  render(request,"basic.html",data)
    except Exception as e:
        print(e)
        return obj.bad_request(message=str(e))

def conatctUs(request):
    try:
        # data = (request)
        print("contact")
        n1 = request.GET['num1']
        n2 = request.GET['num2']
        print(n1+n2)
        return render(request,"contactPage.html")
    except Exception as e:
       pass
        




# def custom_bingo(request):
#     return render(request, "bingo/pages/custom_bingo.html")

def get_custom_bingo(request):

    print("get_custom_bingo")
    # a = request.POST.getlist('arr[]')
    # arr_lis = app_models.custom_shuff(a, 150, True) #function imported from models.py
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = f'inline; filename="bingo.pdf"'
    # buffer = io.BytesIO() 
    # doc = SimpleDocTemplate(buffer, pagesize = letter)
    # # container for the 'Flowable' objects
    # elements = []
    # for arr in arr_lis:
    #     data = arr
    #     t = Table(data, 5 * [1.5 * inch], 6 * [1.4 * inch])
    #     # from (column, row) to (column, row)
    #     t.setStyle(TableStyle([...])) #table styles here
    #     elements.extend([t, PageBreak()])
    # # write the document to disk
    # doc.build(elements)
    # response.write(buffer.getvalue())
    # buffer.close()
    return response

class  Conversion_FileUploadviews(View):    
     def post(self,request):
        try:
            # obj= mainclass()
            # Conversion_Exchange = request.POST['Conversion_Exchange']

            file = request.FILES['myfileToConversion']
            print('file',file)
            # datapd = pd.read_csv(file)
            # print('datapd',datapd)
            
            # data = obj.get_client_info(request)

            # SendTel().TelegramMsg(
            #         "File Conversion Details of "+str(Conversion_Exchange)+
            #         "\nUSERNAME :"+str(request.user.username)+
            #         "\nIP :"+str(data['ip'])+
            #         "\ndevice :"+str(data['device_type'])+
            #         "\nOS :"+str(data['os_type'])+
            #         "\nOS VERSION :"+str(data['os_version'])+
            #         "\nBROWSER :"+str(data['browser_type'])+
            #         "\nBROWSER VERSION :" +str(data['browser_version'])+
            #         "\nTIME : "+str(datetime.now()),'ClientConfig_bot')
            response = HttpResponse(file, content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename="{0}"'.format(file.name)
    
            return response
            # return  datapd
        except Exception as e:
            print(e)
            # return obj.bad_request(message=str(e))

