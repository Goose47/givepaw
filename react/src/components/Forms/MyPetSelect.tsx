import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchPets, selectPets } from '../../redux/slices/PetsSlice';
import { Pet } from '../global/PetItem'; 
import PetItem from '../global/PetItem';


const PetSelect = () => {
  const dispatch = useDispatch();
  const pets = useSelector(selectPets);

  useEffect(() => {
    dispatch(fetchPets() as any);
  }, [dispatch]);

  return (
    pets && (
      <div>
        {pets.map((pet: Pet) => (
                <div className="Profile__Item">
                  <PetItem pet={pet} />
                </div>
              ))}
      </div>
    )
  );
};

export default PetSelect;
