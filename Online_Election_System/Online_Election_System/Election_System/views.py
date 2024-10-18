from django.shortcuts import render, redirect
from .forms import NewregistrationForm,VoterregistrationForm,VoteForm
from .models import Newregistration,Voterregistration,Completedvote,Result
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='login_view_url')
def registration_view(request):
    form = NewregistrationForm()
    template_name ='Election_System/registration.html'
    if request.method == 'POST':
        form = NewregistrationForm(request.POST)
        if form.is_valid():
            form.save()
            vid = form.cleaned_data['voterid']
            fn = form.cleaned_data['fullname']
            vote = Completedvote(voterid=vid, fullname=fn)
            vote.save()
            return redirect('show_registration_view_url')

    form = NewregistrationForm()
    context = {'form':form}
    return render(request, template_name, context)

@login_required(login_url='login_view_url')
def show_registration_view(request):
    data = Newregistration.objects.all()
    template_name ='Election_System/show_registration.html'
    context = {'data':data}
    return render(request, template_name, context)

def update_view(request,nm):
    obj = Newregistration.objects.get(fullname=nm)
    form = NewregistrationForm(instance=obj)
    template_name = 'Election_System/registration.html'
    if request.method == 'POST':
        form = NewregistrationForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_registration_view_url')
    context = {'form':form}
    return render(request, template_name, context)

def delete_view(request,nm):
    obj = Newregistration.objects.get(fullname=nm)
    obj.delete()
    return redirect('show_registration_view_url')


@login_required(login_url='login_view_url')
def voter_registration_view(request):
    template_name = 'Election_System/voterregistration.html'
    if request.method == 'POST':
        form = VoterregistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            fn = form.cleaned_data['fullname']
            ptynm = form.cleaned_data['partynm']
            pryimg = form.cleaned_data['partyimg']
            res = Result(fullname=fn, partynm=ptynm, partyimg=pryimg, vote=0)
            res.save()
            return redirect('voter_show_registration_view_url')
    else:
        form = VoterregistrationForm()
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login_view_url')
def voter_show_registration_view(request):
    data = Voterregistration.objects.all()
    template_name = 'Election_System/show_voterregistration.html'
    context = {'data': data}
    return render(request, template_name, context)

def voter_update_view(request, nm):
    obj = Voterregistration.objects.get(fullname=nm)
    form = VoterregistrationForm(instance=obj)
    template_name = 'Election_System/voterregistration.html'
    if request.method == 'POST':
        form = VoterregistrationForm(request.POST,request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_registration_view_url')
    context = {'form': form}
    return render(request, template_name, context)

def voter_delete_view(request, nm):
    obj = Voterregistration.objects.get(fullname=nm)
    obj.delete()
    return redirect('voter_show_registration_view_url')

@login_required(login_url='login_view_url')
def voter_view(request):
    form = VoteForm()
    template_name = 'Election_System/vote.html'

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            voterid = form.cleaned_data['voterid']
            fullname = form.cleaned_data['fullname']

            try:
                voter = Newregistration.objects.get(voterid=voterid)
                if voter.fullname == fullname:
                    try:
                        existing_vote = Completedvote.objects.get(voterid=voterid)
                        if existing_vote.vote == 'voting complete':
                            messages.error(request, 'You have already completed voting.')
                        else:
                            existing_vote.vote = 'voting complete'
                            existing_vote.save()
                            return redirect('voteing_view_url')
                    except Completedvote.DoesNotExist:
                        return redirect('voter_view_url')
                else:
                    messages.error(request, 'Invalid Name.')
            except Newregistration.DoesNotExist:
                messages.error(request, 'Invalid Voter Id')
        else:
            messages.error(request, 'Invalid input data.')

    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login_view_url')
def voteing_view(request):
    template_name = 'Election_System/voteing.html'

    if request.method == 'POST':
        fullname = request.POST.get('fn')

        try:
            vote_entry = Result.objects.get(fullname=fullname)
            print('Done bro!')
            vote_entry.vote += 1
            vote_entry.save()

            return redirect('votingcomplete_view_url')

        except Result.DoesNotExist:
            messages.error(request, 'Invalid fullname')

    else:
        print('What the fuck!')

    data = Voterregistration.objects.all()
    context = {'data': data}
    return render(request, template_name, context)


def votingcomplete_view(request):
    template_name = 'Election_System/votingcomplete.html'
    data = Voterregistration.objects.all()
    context = {'data': data}
    return render(request, template_name, context)

@login_required(login_url='login_view_url')
def showcompletedvote_view(request):
    data = Completedvote.objects.all()
    template_name = 'Election_System/showcompletedvote.html'
    context = {'data': data}
    return render(request, template_name, context)

def update_completedvote_view(request):
    completed_votes = Completedvote.objects.all()

    for vote_instance in completed_votes:
        vote_instance.vote = 'none'
        vote_instance.save()

    return redirect('showcompletedvote_view_url')

@login_required(login_url='login_view_url')
def show_result_view(request):
    data = Result.objects.all()
    template_name ='Election_System/show_result.html'
    context = {'data':data}
    return render(request, template_name, context)

def update_result_view(request):
    result_votes = Result.objects.all()

    for vote_instance in result_votes:
        vote_instance.vote = 0
        vote_instance.save()

    return redirect('show_result_view_url')
