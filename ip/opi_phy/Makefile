IPS_ROOT ?= $(shell realpath ../)

include filelist.mk
include $(IPS_ROOT)/prim/filelist.mk

EXTRA_SIM_ELAB_FILES = 

EXTRA_SIM_FILES = \
	$(wildcard $(IPS_ROOT)/simlib/rtl/*.sv)

.PHONY: lint
lint:
	@verilator -sv -Wno-fatal -F $(IPS_ROOT)/../lint/filelist.f $(FILELIST) && echo "Lint OK"

.PHONY: sv2v
sv2v: lint
	@mkdir -p build
	@sv2v $(FILELIST) $(EXTRA_SIM_ELAB_FILES) -w build/top.v -DSIMULATION
	@verilator -sv -lint-only --bbox-unsup -Wno-fatal lint/waiver.vlt $(EXTRA_SIM_FILES) build/top.v

TEST_NAME ?= tc1
.PHONY: tb
tb: sv2v
	@mkdir -p build/tb/$(TEST_NAME)
	@iverilog \
		-g2012 -Wno-anachronisms \
		-s tb \
		-DSIMULATION -DCACHE_CTRL_TB \
		$(EXTRA_SIM_FILES) \
		dv/tb/$(TEST_NAME)/tb.sv \
		build/top.v -o build/tb/$(TEST_NAME)/tb.out
	@cd build/tb/$(TEST_NAME) && vvp tb.out -fst-speed
