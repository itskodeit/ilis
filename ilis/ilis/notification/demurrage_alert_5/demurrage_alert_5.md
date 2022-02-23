{% if doc.storage_days <= 0 %}
    Free storage days for stuffed container have ended, Already incurred {{doc.storage_days}} Charged days.
{% elif doc.storage_days <= 5 %}
    Be ware only {{doc.storage_days}} free storage days left for stuffed container.
{% else %}
    Free storage {{doc.storage_days}} days left for stuffed container.
{% endif %}
