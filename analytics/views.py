from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import Account
from .api import RiotAPI


# Create your views here.


def info(request):
    acc = request.GET['acc']
    reg = request.GET['srv']

    res = RiotAPI(reg).get_account(acc)

    if not res.status_code == 200:
        return render(request, 'summoner-not-found.html', {
            'name': acc
        })

    acc_info = res.json()

    try:
        account = Account.objects.get(name=acc_info['name'], server=reg)
    except ObjectDoesNotExist as e:
        account = Account.objects.create(
            name=acc_info['name'],
            server=reg,
            account_id=acc_info['accountId'],
            summoner_id=acc_info['id'],
            icon_id=acc_info['profileIconId'],
            summoner_level=acc_info['summonerLevel'],
        )

    return render(request, 'summoner-info.html', {
        'account': account,
        'region': reg
    })
