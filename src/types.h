/*
 *  types.h - Definitions of data types
 *
 *  SIDPlayer (C) Copyright 1996-2004 Christian Bauer
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#ifndef TYPES_H
#define TYPES_H

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#if defined(__BEOS__)
#include <support/SupportDefs.h>
#elif defined(SDL)
#include <SDL_types.h>
typedef Uint8 uint8;
typedef Sint8 int8;
typedef Uint16 uint16;
typedef Sint16 int16;
typedef Uint32 uint32;
typedef Sint32 int32;
typedef Uint64 uint64;
typedef Sint64 int64;
#endif

// Cycle count
typedef uint32 cycle_t;
const cycle_t CYCLE_NEVER = 0xffffffff;	// Infinitely into the future

#endif
