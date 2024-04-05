from pysmt.environment import Environment
from pysmt.logics import Logic
from pysmt.smtlib.solver import SmtLibSolver
from pysmt.solvers.interpolation import Interpolator


class SmtLibInterpolator(Interpolator):

    solver: SmtLibSolver

    def __init__(self, args: list[str], environment: Environment, logic: Logic, 
                 LOGICS: list[Logic] | None = None, **options):
        super().__init__()
        self.solver = SmtLibSolver(args, environment, logic, LOGICS,
                                   **options | {'solver_options': {':produce-interpolants': 'true'}})

    def _exit(self):
        self.solver.exit()
