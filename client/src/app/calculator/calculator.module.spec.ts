import { CalculatorModule } from './calculatorR.module';

describe('CalculatorModule', () => {
  let calculatorModule: CalculatorModule;

  beforeEach(() => {
    calculatorModule = new CalculatorModule();
  });

  it('should create an instance', () => {
    expect(calculatorModule).toBeTruthy();
  });
});
