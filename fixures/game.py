import pytest

@pytest.fixture
def questions():
    q_about = dict(id='about', type='about', text='What?')
    q_company = dict(id='companydetails', type='company-details', text='Who?')
    q_dates = dict(id='dates', type='dates', text='When?')
    q_roling = dict(id='rolling', type='rolling', text='How much?')

    q_checklist = dict(id='checklist', type='checklist', text='Check List')
    q_checklist_2 = dict(id='checklist2', type='checklist', text='Chec list 2')
    q_bingo = dict(id='bingo', type='bingo', text='Bingo')
    q_freeform = dict(id='freeform', type='freeform', text='Whatever?')
    q_freeform_2 = dict(id='freeform2', type='freeform', text='Free')

    return [
        q_about,
        q_company,
        q_dates,
        q_roling,
        q_checklist,
        q_checklist_2,
        q_bingo,
        q_freeform,
        q_freeform_2
    ]


@pytest.fixture
def typed_answers():
    def ans(id, v): return dict(id=id, at='123', value=v)

    return dict(
        about = ans('about', {'age': '31', 'gender': 'male', 'preference': 'straight'}),
        companydetails = ans('companydetails', {'partner': False, 'malefriends': {'count': 4},
            'femalefriends': {'count': 3}, 'kids': {'boys': 3, 'girls': 34},
            'details': 'fsa'
            }),

        dates = ans('dates', {'start': '1434924000000', 'end': '1435183200000', 'flexible': True}),
        rolling = ans('rolling', 4),
        checklist = ans('checklist', ['Some', 'Body', 'Extra note always last']),
        checklist_2 = ans('checklist2', ['Somez', 'Thingzsz', '']),
        bingo = ans('bingo', ['Pedicure', 'Fifth gorilla chant', 'Extranoteaslo']),
        freeform = ans('freeform', 'Knock the blast'),
        freeform_2 = ans('freeform2', 'Cinderella'),
    )



@pytest.fixture
def user_answers(typed_answers):
    return typed_answers.values()
