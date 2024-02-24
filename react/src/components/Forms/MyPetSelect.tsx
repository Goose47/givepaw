import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchPets, selectPets } from "../../redux/slices/PetsSlice";
import PetItem, { Pet } from "../global/PetItem";
import { FaPlus } from "react-icons/fa6";

interface MyPetSelectProps {
  onAppend: () => void
  onSelect: (value: number) => void
}

const MyPetSelect = (props : MyPetSelectProps) => {
  const dispatch = useDispatch();
  const pets = useSelector(selectPets);

  useEffect(() => {
    dispatch(fetchPets() as any);
  }, [dispatch]);

  return (
    <div>
      {pets.length > 0 ? (
        <div className="Profile__Pets">
          <h3>Выберите своего питомца:</h3>
          <div className="Profile__Row">
            {pets.map((pet: Pet) => (
              <div className="Profile__Item" onClick={() => props.onSelect(pet.id)}>
                <PetItem selectable pet={pet} />
              </div>
            ))}
            <div className="Profile__Item">
              <div className="PetItem__Add">
                <div className="PetItem__Add__Icon" onClick={props.onAppend}>
                  <FaPlus />
                </div>
              </div>
            </div>
          </div>
        </div>
      ) : (
        <h4>;ksflgkhjwe</h4>
      )}
    </div>
  );
};

export default MyPetSelect;
