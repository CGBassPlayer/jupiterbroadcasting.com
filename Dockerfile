FROM ghcr.io/gohugoio/hugo:v0.169.0 AS builder
# this defaults to an empty variable
ARG BASE_URL
COPY --chown=hugo:hugo . /site
WORKDIR /site
# when the argument is empty or PROD, do a normal production build
#   else if it's TESTS_WEB use the specified baseURL "/", or
#   exit 1, because that use case hasn't been provided
#   https://explainshell.com/ is an awesome website which can explain this in more detail
#   set -x : changes the shell's default verbosity and puts it in "debug" mode
RUN set -x && ( [ -z "${BASE_URL}" ] || [ "${BASE_URL}" == "PROD" ] ) \
    && hugo --gc \
    || ( [ "${BASE_URL}" == 'TESTS_WEB' ] && hugo --gc --baseURL "/" || exit 1 )

FROM nginx:1.31.8-alpine
RUN rm -rf /usr/share/nginx/html/*
RUN sed -i 's/#error_page/error_page/' /etc/nginx/conf.d/default.conf
COPY --from=builder /site/public /usr/share/nginx/html
