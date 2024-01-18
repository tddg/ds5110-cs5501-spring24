---
layout: page
title: Staff
description: A listing of all the course staff members.
nav_order: 4
---

# Staff

## Office Hours

Office hours will be held virtually on Zoom.

Links to join the TA and instructor office hours are posted in Canvas.

## Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

{% assign teaching_assistants = site.staffers | where: 'role', 'Teaching Assistant' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}

## Teaching Assistant

{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}
