from django.test import TestCase
from builder.models import *

class ModuleTests(TestCase):

    def test_string_representation(self):
        """String representation of a module should be its title"""
        core_prog = Module(title="Core Programming")
        self.assertEqual(str(core_prog), core_prog.title)

    def test_add_prerequisites(self):
        """A module should be able to have more than 1 prerequisite"""
        core_prog = Module(title="Core Programming")
        soft_dev = Module(title="Software Development")
        professional_dev = Module(title="Professional Development")
        core_prog.save()
        soft_dev.save()
        professional_dev.save()
        soft_dev.prerequisites.add(core_prog)
        soft_dev.prerequisites.add(professional_dev)


        results = [str(module)for module in soft_dev.prerequisites.all()]
        self.assertEqual(results, [core_prog.title, professional_dev.title])

    def test_retrieve_prerequisite_of(self):
        """A module should be know what is it a prerequisite for"""
        soft_dev = Module(title="Software Development")
        soft_dev.save()
        professional_dev = Module(title="Professional Development")
        professional_dev.save()
        soft_dev.prerequisites.add(professional_dev)
        self.assertEqual(professional_dev.is_prerequisite_of.all()[0], soft_dev)


class ProgrammeTests(TestCase):

    def test_string_representation(self):
        """String representation of a programme should be its name"""
        prog = Programme(name="Computer Science")
        self.assertEqual(str(prog), prog.name)

    def test_adding_modules(self):
        """Should be able to add many modules to a programme"""
        core_prog = Module(title="Core Programming")
        core_prog.save()
        soft_dev = Module(title="Software Development")
        soft_dev.save()
        cs = Programme(name="Computer Science")
        cs.save()
        cs.modules.add(core_prog, soft_dev)
        prog_content = [str(module)for module in cs.modules.all()]
        self.assertEqual(prog_content, [core_prog.title, soft_dev.title])


class CriteriaTests(TestCase):

    def test_plural_name(self):
        """Plural should display as Criteria, not Criterions"""
        self.assertEqual(str(Criterion._meta.verbose_name_plural), "Criteria")


class AccreditationTests(TestCase):

    def test_string_representation(self):
        accreditation = Accreditation(name="BCS2")
        self.assertEqual(str(accreditation), accreditation.name)

    def test_adding_criteria(self):
        """An accreditation should be able to add different crtieria"""
        accreditation = Accreditation(name="BCS2")
        accreditation.save()
        cr1 = Criterion(code="BCS100")
        cr1.save()
        cr2 = Criterion(code="BCS101")
        cr2.save()
        accreditation.criteria.add(cr1)
        accreditation.criteria.add(cr2)
        criteria = [str(criterion) for criterion in accreditation.criteria.all()]
        self.assertEqual(criteria, [cr1.code, cr2.code])














