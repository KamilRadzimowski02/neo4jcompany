from neo4j import GraphDatabase


class Database:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def getEmployees(self):
        with self.driver.session() as session:
            return session.read_transaction(self._get_employees)

    @staticmethod
    def _get_employees(tx):
        result = tx.run('MATCH (m:Employee) RETURN m').data()
        return result

    def addEmployee(self, name, department):
        with self.driver.session() as session:
            return session.execute_write(self._add_employee, name, department)

    @staticmethod
    def _add_employee(tx, name, department):
        result = tx.run("CREATE (a:Employee) "
                        "SET a.name = $name, "
                        "SET a.department = $department "
                        "RETURN a", name=name, department=department)
        return result.single()

    @staticmethod
    def _delete_employee(tx, id):
        result = tx.run('MATCH (m:Employee) WHERE m.id=$id DETACH DELETE m')

