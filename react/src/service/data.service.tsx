import axios from 'axios';

export const getBreeds = async () => {
  try {
    const response = await axios.get('pets/breeds');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getBloodTypes = async (pet_type_id: number) => {
  try {
    const response = await axios.get(`blood_group/${pet_type_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
export const getVaccines = async () => {
  try {
    const response = await axios.get('pets/vaccinations');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getAnimalTypes = async () => {
  try {
    const response = await axios.get('pets/pet_types');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getClinics = async () => {
  try {
    const response = await axios.get('clinics');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const createPet = async () => {
    try {
      const response = await axios.post('pets');
      return response.data;
    } catch (error) {
      console.error(error);
    }
  };

export const createdDonor = async (pet_id: number, city_id: number, clinic_id: number) => {
  try {
    const response = await axios.post('donors');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const createRecipient = async (reason: string, blood_component_id: number, blood_amount: number, donor_amount: number,
    pet_id: number, clinic_id: number, end_actual_date: string) => {
  try {
    const response = await axios.post('recipients');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getPets = async () => {
  try {
    const response = await axios.get('pets/my');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
