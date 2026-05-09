export const getScoreColor = (score: number) => {
  if (score >= 49) return "text-green-600 bg-green-100";
  if (score >= 25) return "text-yellow-600 bg-yellow-100";
  return "text-red-600 bg-red-100";
};
