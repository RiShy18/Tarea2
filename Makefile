all: build run

clean:
	rm -rf ./*.bin
build:
	nasm -fbin kernel.asm -o kernel.bin
	nasm -fbin bootloader.asm -o bootloader.bin
	cat bootloader.bin kernel.bin > bootableTanks.bin
run:
	qemu-system-i386 bootableTanks.bin