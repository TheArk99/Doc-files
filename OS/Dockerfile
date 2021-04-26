FROM randomdude/gcc-cross-x86_64-elf

RUN apt-get update
RUN apt-get upgrade -Y
RUN apt-get install -Y nasm
RUN apt-get install -Y xorriso
RUN apt-get install -Y grub-pc-bin
RUN apt-get install -Y grub-common

VOLUME /root/env
WORKDIR /root/env
