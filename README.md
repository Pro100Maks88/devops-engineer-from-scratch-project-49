#### Python :snake:
### Hexlet tests and linter status:
[![Actions Status](https://github.com/Pro100Maks88/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Pro100Maks88/devops-engineer-from-scratch-project-49/actions)

# SonarQube

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Pro100Maks88_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Pro100Maks88_devops-engineer-from-scratch-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Pro100Maks88_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Pro100Maks88_devops-engineer-from-scratch-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Pro100Maks88_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Pro100Maks88_devops-engineer-from-scratch-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Pro100Maks88_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Pro100Maks88_devops-engineer-from-scratch-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Pro100Maks88_devops-engineer-from-scratch-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Pro100Maks88_devops-engineer-from-scratch-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Pro100Maks88_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Pro100Maks88_devops-engineer-from-scratch-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Pro100Maks88_devops-engineer-from-scratch-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Pro100Maks88_devops-engineer-from-scratch-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Pro100Maks88_devops-engineer-from-scratch-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Pro100Maks88_devops-engineer-from-scratch-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Pro100Maks88_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Pro100Maks88_devops-engineer-from-scratch-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Pro100Maks88_devops-engineer-from-scratch-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Pro100Maks88_devops-engineer-from-scratch-project-49)

## :scroll: Игры разума (Brain Games)
   Набор Brain Games включает пять консольных математических игр. Их цель — развить мышление и проверить математические навыки. Механика проста: в каждой игре нужно безошибочно ответить на три вопроса подряд.

## :joystick: Коллекция игр 
   1. **brain-calc** — Вычисление результата выражения
   2. **brain-even** — Определение четности числа
   3. **brain-gcd** — Нахождение наибольшего общего делителя
   4. **brain-prime** — Определение простого числа
   5. **brain-progression** — Поиск пропущенного числа в арифметической прогрессии

## :low_battery: Минимальные требования
   - **Python** версии 3.10 и выше
   - **pip** или **uv** для управления зависимостями
   - **Git** для клонирования репозитория

## :closed_book: Инструкции по установке и запуску
   Важно: перед установкой убедитесь, что на вашем компьютере уже установлен Python — сам uv не зависит от Python, но требует Python‑окружения для работы с зависимостями

   ```bash
   # Установите пакетный менеджер uv
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Используя менеджер пакетов
   pipx install uv

   # Пользователи MacOS также могут поставить через Homebrew
   brew install uv

   # Клонируйте репозиторий
   git clone https://github.com/Pro100Maks88/devops-engineer-from-scratch-project-49.git
   
   # Перейдите в папку с игрой
   cd devops-engineer-from-scratch-project-49

   После установки можно запустить игру командой:
   # Запуск игры
   
   brain-calc #Вычисление результата выражения
   brain-even #Определение четности числа
   brain-gcd #Нахождение наибольшего общего делителя
   brain-prime #Определение простого числа
   brain-progression #Поиск пропущенного числа в арифметической прогрессии
   ```
## :bookmark: Правила игры
  Общее правило для всех игр: нужно дать 3 правильных ответа подряд.
   ### 1. **Brain-Calc**
  Суть игры в следующем: пользователю показывается случайное математическое выражение, например, 35 + 16, которое нужно вычислить и записать правильный ответ. Доступны матемаические выражения (+, -, *)
   ### 2. **Brain-Even**
  Суть игры в следующем: пользователю показывается случайное число. И ему нужно ответить yes, если число чётное, или no — если нечётное.
   ### 3. **Brain-GCD**
  Суть игры в следующем: пользователю показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.
   ### 4. **Brain-Prime**
  Суть игры в следующем: пользователю показывается случайное число. И ему нужно ответить yes, если число простое, или no, если оно составное.
   ### 5. **Brain-Progression**
  Суть игры в следующем: пользователю показывается ряд чисел, который образует арифметическую прогрессию с одним пропущенным числом, пользователь должен определить и ввести пропущенное число. Пример: 5 7 9 11 13 .. 17 19 21 23 ответ: 15

## :film_strip: Знакомство с играми
  В этом разделе можно посмотреть примеры всех игр.
  
  ***Brain-Calc***

  ***Brain-Even***

  ***Brain-GCD***

  ***Brain-Prime***

  ***Brain-Progression***
  
#### Автор 
       Maxim Golovin
       Проект был создан в рамках обучениюя на платформе Hexlet.io
   
