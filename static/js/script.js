// Toggle feature list expansion on pricing page
function toggleFeatures(packageType) {
    const features = document.getElementById(packageType + '-features');
    const icon = document.getElementById(packageType + '-icon');

    features.classList.toggle('expanded');
    icon.classList.toggle('rotated');
}
