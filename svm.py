import numpy as np

def manual_svm_example():
    print("САМЫЙ ПРОСТОЙ SVM")
    print("=" * 40)
    
    X = np.array([
        [170, 65], [175, 70], [180, 75],  # Высокие (1)
        [160, 55], [155, 50], [165, 60]   # Низкие (0)
    ])
    y = np.array([1, 1, 1, 0, 0, 0])
    
    print("Данные:")
    for i in range(len(X)):
        print(f"  Человек {i+1}: рост {X[i,0]}см, вес {X[i,1]}кг -> {'Высокий' if y[i] == 1 else 'Низкий'}")
    
    w = np.array([2, -1])  # Веса: важность роста и веса
    b = -250               # Смещение
    
    print(f"\nРазделяющая функция: {w[0]}*рост + {w[1]}*вес + {b} = 0")
    
    # Предсказания
    predictions = []
    for i in range(len(X)):
        decision = w[0]*X[i,0] + w[1]*X[i,1] + b
        prediction = 1 if decision > 0 else 0
        predictions.append(prediction)
        
        print(f"  Человек {i+1}: {decision:6.1f} -> {'Высокий' if prediction == 1 else 'Низкий'}")
    
    accuracy = np.mean(np.array(predictions) == y)
    print(f"\nТочность: {accuracy:.1%}")

# Запуск
manual_svm_example()