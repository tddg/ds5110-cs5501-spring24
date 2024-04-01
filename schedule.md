---
layout: schedule
title: Course Schedule 
description: Being less concrete further out, the course scheduling is tentative and subject to changes.
nav_order: 2
weeks:
  # Each key in this dictionary is a week, and then eaach week has a key in [Mon, Tue, Wed, Thu, Fri].
  # Each day has keys `date` and `content`. The date is shown on the schedule, and `content` is a key into the yml file in \_data/modules.yml. `content` may be an array.
  # Each day can also have a `note` field, which is shown in italics on the calendar.
  # This schedule data is unioned with the deadlines in \_data/config.yml
  '1':
    Mon:
      date: 2024/01/15
      content: 1a
    Wed:
      date: 2024/01/17
      content: 1b
  '2':
    Mon:
      date: 2024/01/22
      content: 2a
      note: "[Assignment 0](/ds5110-cs5501-spring24/assignments/a0) out"
    Wed:
      date: 2024/01/24
      content: 2b
  '3':
    Mon:
      date: 2024/01/29
      content: 2c
    Wed:
      date: 2024/01/31
      content: 2d
      note: "[Assignment 1](/ds5110-cs5501-spring24/assignments/a1) out"
  '4':
    Mon:
      date: 2024/02/05
      content: 3a
    Wed:
      date: 2024/02/07
      content: 3b
  '5':
    Mon:
      date: 2024/02/12
      content: 4a
    Wed:
      date: 2024/02/14
      content: 4b
      note: "[Assignment 2](/ds5110-cs5501-spring24/assignments/a2) out"
  '6':
    Mon:
      date: 2024/02/19
      content: 5a
    Wed:
      date: 2024/02/21
      content: 5b
  '7':
    Mon:
      date: 2024/02/26
      content: midtermReview
    Wed:
      date: 2024/02/28
      content: midterm
      note: "[Assignment 3](/ds5110-cs5501-spring24/assignments/a3) out"
  '8':
    Mon:
      date: 2024/03/04
      content: springRecess
    Wed:
      date: 2024/03/06
      content: springRecess
  '9':
    Mon:
      date: 2024/03/11
      content: 6a
    Wed:
      date: 2024/03/13
      content: 6b
  '10':
    Mon:
      date: 2024/03/18
      content: 7a
    Wed:
      date: 2024/03/20
      content: 7b
  '11':
    Mon:
      date: 2024/03/25
      content: 8a
    Wed:
      date: 2024/03/27
      content: 8b
  '12':
    Mon:
      date: 2024/04/01
      content: 8c
    Wed:
      date: 2024/04/03
      content: 9a
  '13':
    Mon:
      date: 2024/04/08
      content: 10a
    Wed:
      date: 2024/04/10
      content: 10b
  '14':
    Mon:
      date: 2024/04/15
      content: 10c
    Wed:
      date: 2024/04/17
      content: 10d
  '15':
    Mon:
      date: 2024/04/22
      content: workOnProj
    Wed:
      date: 2024/04/24
      content: presentation
  '16':
    Mon:
      date: 2024/04/29
      content: presentation
    Wed:
      date: 2024/05/01
      content: 
---
