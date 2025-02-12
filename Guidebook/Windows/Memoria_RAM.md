# Obter Informações da Memória RAM no PowerShell

## Introdução
O comando abaixo permite visualizar detalhes sobre os módulos de memória RAM instalados no sistema usando o PowerShell:

```powershell
Get-CimInstance Win32_PhysicalMemory | Select-Object Manufacturer, PartNumber, Speed, ConfiguredClockSpeed, @{Name="CapacityGB"; Expression={[math]::round($_.Capacity / 1GB, 2)}}, Voltage, DeviceLocator, BankLabel, FormFactor, @{Name="MemoryType"; Expression={if ($_.MemoryType -eq 0) {"DDR4"} elseif ($_.MemoryType -eq 1) {"DDR"} elseif ($_.MemoryType -eq 2) {"SDRAM"} elseif ($_.MemoryType -eq 3) {"DDR2"} elseif ($_.MemoryType -eq 4) {"DDR3"} elseif ($_.MemoryType -eq 5) {"LPDDR"} elseif ($_.MemoryType -eq 6) {"LPDDR2"} elseif ($_.MemoryType -eq 7) {"LPDDR3"} elseif ($_.MemoryType -eq 8) {"LPDDR4"} else {"Unknown"}}}

