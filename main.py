class CpfGenerator:
    def __init__(self):
        ...
    
    def generate_nine_digits(self) -> str:
        """Gera os nove primeiros digitos de base do CPF

        Returns:
            str: Nove primeiros digitos do CPF
        """
        from string import digits
        from random import sample
        
        base_digits = sample(digits, 9)
        base_digits = ''.join(base_digits)
        return base_digits
    
    def generate_digit1(self, base: str) -> str:
        """Gera o primeiro digito do CPF

        Args:
            base (str): Nove primeiros digitos base do CPF

        Returns:
            str: Valor do primeiro digito gerado.
        """
        base_digits = base
        m, s = 10, 0
        for digit in base_digits:
            s += int(digit) * m
            m -= 1
        result = str(11 - s % 11)
        return result if int(result) <= 9 else '0'
    
    def generate_digit2(self, base: str, digit1: str) -> str:
        """Gera o segundo digito do CPF

        Args:
            base (str): Os nove digitos base do CPF
            digit1 (str): O primeiro digito gerado do CPF

        Returns:
            str: O valor do segundo digito gerado
        """
        base_digits = base + digit1
        m, s = 11, 0
        for digit in base_digits:
            s += int(digit) * m
            m -= 1
        result = str(11 - s % 11)
        return result if int(result) <= 9 else '0'
    
    def generate(self) -> str:
        """Gera um novo CPF randomicamente

        Returns:
            str: Um CPF valido randomizado e formatado.
        """
        base = self.generate_nine_digits()
        digit_1 = self.generate_digit1(base)
        digit_2 = self.generate_digit2(base, digit_1)
        generated_cpf = base + digit_1 + digit_2
        cpf_formatted = self.formatter(generated_cpf)
        return cpf_formatted

    def formatter(self, cpf: str):
        """Realiza a formatação do CPF no formato xxx.xxx.xxx-xx

        Args:
            cpf (str): CPF gerado somente numeros

        Returns:
            str: CPF formatado no padrao xxx.xxx.xxx-xx
        """
        cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        return cpf
        

if __name__ == '__main__':
    cpf = CpfGenerator()
    print(cpf.generate())
    