
# created by rvcgeeks <github.com/rvcgeeks> (linkedin.com/in/rvchavadekar) @ Pune, India

from django.shortcuts import render, redirect
from django.http import JsonResponse
from psutil import cpu_percent, virtual_memory


class UtilFrame:
    
    def __init__(self, numframes, callback):
        
        self._N =  numframes
        self._callback = callback
        self._frame = [0] * self._N
        
    def __call__(self):
        
        self._frame.pop(0)
        self._frame.append(self._callback())
        return self._frame
        

NumFrames = 250
cpu_util_frame = UtilFrame(NumFrames, cpu_percent)
ram_util_frame = UtilFrame(NumFrames, lambda : virtual_memory().percent)


def render_all_charts(request):
    
    try:
        request.session['id'] # check login or not
    except KeyError:
        return redirect('/success') # the success methods will bump to login after a KeyError again
    
    return render(request, 'mycharts.html', {
        'secs_labels': [ NumFrames - i for i in range(NumFrames) ],
        'cpu_util_frame': cpu_util_frame(),
        'ram_util_frame': ram_util_frame(),
    })


def update_charts(request):
    
    my_response = {
        'cpu_frame': cpu_util_frame(),
        'ram_frame': ram_util_frame()
    }
    
    return JsonResponse(my_response)
    
    
