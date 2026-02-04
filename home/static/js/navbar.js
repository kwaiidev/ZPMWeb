const navs = [
    {
        Text: 'Home',
        Url: '#home',
        Class: 'home',
        Alt: 'Jump to the home section'
    },
    {
        Text: 'About',
        Url: '#about',
        Class: 'about',
        Alt: 'Jump to the About ZPM section'
    },
    {
        Text: 'How?',
        Url: '#how',
        Class: 'How',
        Alt: 'Jump to the Hows section'
    },
    {
        Text: 'Products',
        Url: '#products',
        Class: 'products',
        Alt: 'Jump to the Products section'
    }
];

const rootUrl =
    window.location.origin && window.location.origin !== 'null'
        ? `${window.location.origin}/`
        : '/';

// Loop that places list items to create the nav bar.
const navBarMarkup = navs
    .map(
        (nav) =>
            `<li><a href="${rootUrl}${nav.Url}" class="text-xs font-semibold uppercase tracking-[0.3em] text-[#F0F0DB] transition-colors hover:text-[#ACBAC4] md:text-sm ${nav.Class}" aria-label="${nav.Alt}">${nav.Text}</a></li>`
    )
    .join('');

const nav = document.querySelector('#navId');
nav.innerHTML = navBarMarkup;

// Creates hamburger icon for mobile navigation

// Select HTML objects

const burgerButton = document.querySelector('.burger');
const burgerIcon = document.querySelector('.burger i');

// Defining a function

function toggleNav() {
    burgerIcon.classList.toggle('fa-bars');
    burgerIcon.classList.toggle('fa-times');
    nav.classList.toggle('hidden');
}

// Calling the function after click event occurs
burgerButton.addEventListener('click', function () {
    toggleNav();
});