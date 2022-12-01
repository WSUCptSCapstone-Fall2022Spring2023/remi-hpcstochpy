model  = """# Generated by PySCeS 0.8.0 (2012-07-04 09:55)
 
# Keywords
Description: Immigration-Death (002), variant 10
Modelname: ImmigrationDeath09
Output_In_Conc: True
Species_In_Conc: False
 
# GlobalUnitDefinitions
UnitVolume: litre, 1.0, 0, 1
UnitLength: metre, 1.0, 0, 1
UnitSubstance: item, 1.0, 0, 1
UnitArea: metre, 1.0, 0, 2
UnitTime: second, 1.0, 0, 1
 
# Compartments
Compartment: Cell, 1.0, 3 
 
# Reactions
Death@Cell:
    X > $pool
    Mu*X

Immigration@Cell:
    $pool > X
    Alpha
 
# Event definitions
Event: reset, operator.ge(_TIME_,22.5), 0.0 
{
X = 20
}
 
# Fixed species
 
# Variable species
X@Cell = 0.0
 
# Parameters
Mu = 0.1
Alpha = 1.0
""" 

xml_model="""<?xml version="1.0" encoding="UTF-8"?>
<sbml xmlns="http://www.sbml.org/sbml/level2/version4" level="2" version="4">
  <model id="ImmigrationDeath09" name="Immigration-Death (002), variant 10">
    <listOfUnitDefinitions>
      <unitDefinition id="substance">
        <listOfUnits>
          <unit kind="item"/>
        </listOfUnits>
      </unitDefinition>
    </listOfUnitDefinitions>
    <listOfCompartments>
      <compartment id="Cell"/>
    </listOfCompartments>
    <listOfSpecies>
      <species id="X" compartment="Cell" initialAmount="0" hasOnlySubstanceUnits="true"/>
    </listOfSpecies>
    <listOfParameters>
      <parameter id="Alpha" value="1"/>
      <parameter id="Mu" value="0.1"/>
    </listOfParameters>
    <listOfReactions>
      <reaction id="Immigration" reversible="false">
        <listOfProducts>
          <speciesReference species="X"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <ci> Alpha </ci>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="Death" reversible="false">
        <listOfReactants>
          <speciesReference species="X"/>
        </listOfReactants>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> Mu </ci>
              <ci> X </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
    </listOfReactions>
    <listOfEvents>
      <event id="reset">
        <trigger>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <geq/>
              <csymbol encoding="text" definitionURL="http://www.sbml.org/sbml/symbols/time"> t </csymbol>
              <cn> 22.5 </cn>
            </apply>
          </math>
        </trigger>
        <listOfEventAssignments>
          <eventAssignment variable="X">
            <math xmlns="http://www.w3.org/1998/Math/MathML">
              <cn type="integer"> 20 </cn>
            </math>
          </eventAssignment>
        </listOfEventAssignments>
      </event>
    </listOfEvents>
  </model>
</sbml>
"""
