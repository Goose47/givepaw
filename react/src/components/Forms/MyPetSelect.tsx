import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchPets, selectPets } from '../../redux/slices/PetsSlice';
import { Pet } from '../global/PetItem';
import PetItem from '../global/PetItem';

const MyPetSelect = () => {
  const dispatch = useDispatch();
  const pets = useSelector(selectPets);

  useEffect(() => {
    dispatch(fetchPets() as any);
  }, [dispatch]);

  return (
    <div>
      {pets.length > 0 ? (
        <div className="Profile__Pets">
          <h3>Выберите своего питомца: </h3>
          <div className="Profile__Row">
            {pets.map((pet: Pet) => (
              <div className="Profile__Item">
                <PetItem pet={pet} />
              </div>
            ))}
          </div>
        </div>
      ) : (
        <h4>;ksflgkhjwe</h4>
      )}
    </div>
  );
};

export default MyPetSelect;
