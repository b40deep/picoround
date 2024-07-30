GC9A01_MOD_DIR := $(USERMOD_DIR)
SRC_USERMOD += $(addprefix $(GC9A01_MOD_DIR)/, gc9a01.c)
SRC_USERMOD += $(addprefix $(GC9A01_MOD_DIR)/, mpfile.c)
SRC_USERMOD += $(addprefix $(GC9A01_MOD_DIR)/, tjpgd565.c)

CFLAGS_USERMOD += -I$(GC9A01_MOD_DIR) -DMODULE_GC9A01_ENABLED=1 -DMICROPY_PY_FILE_LIKE=1
CFLAGS_USERMOD += -DEXPOSE_EXTRA_METHODS=1