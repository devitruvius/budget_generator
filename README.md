# Project Budget Generator

## Description

This project creates a PDF file with a project budget estimate. The user enters the project description, estimated hours, hourly rate, and estimated deadline, and the code calculates the total estimated value and generates a PDF file with the provided information.

## Usage

1. Clone the repository:

   ```python
   # Bash

   git clone [https://github.com/devitruvius/sistema_gerador_orcamento_consultoria]
   ```

2. Install dependencies:

   ```python
   # Bash

   pip install fpdf
   ```

3. Run the script:

   ```python
   # Bash

   python gerador_orcamento_consultoria.py
   ```
   
4. Enter the project information:
   * Project description
   * Estimated hours
   * Hourly rate
   * Estimated deadline
  
5. The PDF file will be generated in the same directory as the script with the name "orçamento.pdf".

## Features

* User-friendly interface for collecting project information
* Calculation of total estimated value
* Generation of a PDF file with project details

## Requirements

* Python 3.x
* fpdf library

## Example Output

   ```python
   Digite a descrição do projeto: Website Redesign
   Digite o total de horas estimadas: 100
   Digite o valor da hora trabalhada: 50
   Digite o prazo estimado: 30 dias
   Orçamento gerado com sucesso!
   ```

## Additional Notes

* The script uses a template PNG file ("template.png") to create the PDF layout. Make sure to place this file in the same directory as the script.
* You can customize the template file to match your desired design.
* The script can be extended to include additional features, such as generating a detailed breakdown of costs by task or adding more information to the PDF file.

## Contributing

Please feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or suggestions, please feel free to contact me.
