import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchPets, selectPets } from '../../redux/slices/PetsSlice';

const PetSelect = () => {
  const dispatch = useDispatch();
  const pets = useSelector(selectPets);

  useEffect(() => {
    dispatch(fetchPets() as any);
  }, [dispatch]);

  return (
    <div>
      {pets.map((item: any) => {
        return <div>{item.name}</div>;
      })}
    </div>
  );
};

export default PetSelect;
