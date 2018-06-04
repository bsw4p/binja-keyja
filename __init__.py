from binaryninja import *
from keystone import *

def assemble(bv):
    bw = BinaryWriter(bv)
    architecture = ChoiceField('Architecture', ['X86', 'X64', 'ARM', 'ARM_THUMB', 'MIPS32', 'MIPS64', 'PPC32', 'PPC64', 'SPARC32'])
    syntax = ChoiceField('Syntax', ['INTEL', 'ATT'])
    code = MultilineTextField('Code')
    get_form_input([architecture, syntax, code], "Keystone assemble")
    
    ks = Ks(KS_ARCH_X86, KS_MODE_32)

    if syntax.result == "ATT":
        ks.syntax = KS_OPT_SYNTAX_ATT

    encoding, count = ks.asm(code.result)
    for oc in encoding:
        bw.write8(oc)

PluginCommand.register("Keystone assemble", "Assemble using keystone engine", assemble)
