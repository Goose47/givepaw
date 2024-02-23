

@router.get("/pet_blood_group/{animal_type}", response_model=list[MockPetBloodGroupSchema])
async def mock_blood_group(request: Request, animal_type: str):
    return [MockPetBloodGroupSchema(
        id=random.randint(1, 100),
        mock_pet_type=MockPetType(id=random.randint(1, 100), title=animal_type),
        mock_blood_group=MockBloodGroup(id=random.randint(1, 100), title=random.choice(["I", "II", "III"])),
        mock_rhesus_type=MockRhesusType(id=random.randint(1, 100), title=random.choice([
            f"фактор {animal_type} 1",
            f"фактор {animal_type} 2",
            f"фактор {animal_type} 3"
        ]))
    ) for _ in range(10)]