// Takes in a date string in the format YYYY-MM-DD and returns a more user-friendly date string
export const formatDate = (dateString) => {
    const [year, month, day] = dateString.split('-');
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    return `${months[parseInt(month) - 1]} ${parseInt(day)}, ${year}`;
  };
  
  // Takes in a time string in the format HH:MM and returns a more user-friendly time string
  export const formatTime = (timeString) => {
    const [hours, minutes] = timeString.split(':');
    const hours12 = parseInt(hours) > 12 ? parseInt(hours) - 12 : parseInt(hours);
    const amOrPm = parseInt(hours) >= 12 ? 'PM' : 'AM';
    return `${hours12}:${minutes} ${amOrPm}`;
  };
