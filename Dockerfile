FROM python:3.8
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt \
    && perl -e "for(0..10000){print int(rand(2**32)).\"\n\"}" > ints.txt
