def gln_epass():
    """
    Назначение: 
    Получение GLN из EPASS

    Требования:
    - спецификация: SPEC-FEATURE-DELIVERY-NOTE-001
    - требования: FR-DELIVERY-NOTE-CREATE-001 
    """
    pass

def shipper_gln():
    """
    Назначение: 
    Присвоение GLN грузоотправителю

    Требования:
    - спецификация: SPEC-FEATURE-DELIVERY-NOTE-001
    - требования: FR-DELIVERY-NOTE-CREATE-002 
    """
    return gln_epass()

def delivery_note_create():
    """
    Назначение: 
    Создание накладной.

    Требования:
    - спецификация: SPEC-FEATURE-DELIVERY-NOTE-001
    - требования: FR-DELIVERY-NOTE-CREATE-003
    """
    return shipper_gln()